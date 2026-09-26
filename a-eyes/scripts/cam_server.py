#!/usr/bin/env python3
"""a-eyes local camera server — live stills + simple password web UI.

Binds 127.0.0.1:8791 only. Public path is proxied by rootserver_poller at
https://rootserver.rootrecord.cloud/aeyes (tunnel → :8799 → here).

Routes:
  GET  /health
  GET  /current.jpg | /current_ch2.jpg | /current_ch3.jpg | /current_ch4.jpg
  GET  /aeyes  /aeyes/          → login or live 4-channel grid
  POST /aeyes/login             → set auth cookie (password from master-key.env)
  GET  /aeyes/logout
  GET  /aeyes/live/ch{1-4}.jpg  → live grab (auth required)

Password key in /home/rootrecord/master/master-key.env:
  AEYES_PUBLIC_PASSWORD=...
"""
from __future__ import annotations

import hashlib
import hmac
import json
import sys
import threading
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from grab_frame import DB_FRAMES, FramesBusy, grab_jpeg, load_master_key  # noqa: E402

HOST = "127.0.0.1"
PORT = 8791
COOKIE_NAME = "aeyes_session"
COOKIE_MAX_AGE = 60 * 60 * 12  # 12 hours

STILL_ROUTES = {
    "current.jpg": 1,
    "current_ch2.jpg": 2,
    "current_ch3.jpg": 3,
    "current_ch4.jpg": 4,
}

# Last successful JPEG per channel — served when RTSP/lock is busy so the
# browser always gets image/jpeg (never JSON) for <img> tags.
_last_jpeg: dict[int, bytes] = {}
_last_lock = threading.Lock()


def _password() -> str:
    return load_master_key("AEYES_PUBLIC_PASSWORD")


def _session_token(password: str) -> str:
    return hmac.new(
        b"aeyes-public-v1",
        password.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def _expected_token() -> str:
    return _session_token(_password())


def _disk_latest(channel: int) -> bytes | None:
    """Newest frame file for this channel already on disk (from grab_all)."""
    try:
        files = sorted(DB_FRAMES.glob(f"ch{channel}-*.jpg"), key=lambda p: p.stat().st_mtime)
        if not files:
            return None
        data = files[-1].read_bytes()
        return data if len(data) > 500 else None
    except OSError:
        return None


LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>a-eyes</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; min-height: 100vh; display: flex; align-items: center; justify-content: center;
         font-family: system-ui, sans-serif; background: #0b0f14; color: #e8eef5; }
  form { background: #141a22; padding: 2rem; border-radius: 12px; width: min(360px, 92vw);
         border: 1px solid #243041; }
  h1 { margin: 0 0 0.25rem; font-size: 1.25rem; }
  p { margin: 0 0 1.25rem; color: #8b9bb0; font-size: 0.9rem; }
  input { width: 100%; padding: 0.7rem 0.85rem; border-radius: 8px; border: 1px solid #2c3b50;
          background: #0b0f14; color: #e8eef5; font-size: 1rem; }
  button { margin-top: 0.9rem; width: 100%; padding: 0.7rem; border: 0; border-radius: 8px;
           background: #2f6fed; color: #fff; font-weight: 600; cursor: pointer; }
  button:hover { background: #3b7cff; }
  .err { color: #ff8b8b; font-size: 0.85rem; margin-top: 0.75rem; }
</style>
</head>
<body>
  <form method="post" action="/aeyes/login">
    <h1>a-eyes</h1>
    <p>Enter the public password to view live cameras.</p>
    <input type="password" name="password" placeholder="Password" autofocus required/>
    <button type="submit">View cameras</button>
    __ERR__
  </form>
</body>
</html>
"""

LIVE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>a-eyes live</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; background: #0b0f14; color: #e8eef5; font-family: system-ui, sans-serif; }
  header { display: flex; align-items: center; justify-content: space-between;
           padding: 0.75rem 1rem; border-bottom: 1px solid #1c2533; }
  header h1 { margin: 0; font-size: 1.05rem; font-weight: 600; }
  header a { color: #8b9bb0; text-decoration: none; font-size: 0.85rem; }
  header a:hover { color: #e8eef5; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; padding: 0.5rem; }
  @media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
  .cell { background: #141a22; border: 1px solid #243041; border-radius: 10px; overflow: hidden; }
  .label { padding: 0.4rem 0.65rem; font-size: 0.8rem; color: #8b9bb0;
           border-bottom: 1px solid #1c2533; display: flex; justify-content: space-between; }
  .label .st { font-size: 0.75rem; opacity: 0.7; }
  .cell img { display: block; width: 100%; height: auto; background: #000; min-height: 140px;
              object-fit: contain; }
</style>
</head>
<body>
  <header>
    <h1>a-eyes — live</h1>
    <a href="/aeyes/logout">Log out</a>
  </header>
  <div class="grid">
    <div class="cell"><div class="label"><span>Channel 1</span><span class="st" id="s1"></span></div><img id="c1" alt="ch1"/></div>
    <div class="cell"><div class="label"><span>Channel 2</span><span class="st" id="s2"></span></div><img id="c2" alt="ch2"/></div>
    <div class="cell"><div class="label"><span>Channel 3</span><span class="st" id="s3"></span></div><img id="c3" alt="ch3"/></div>
    <div class="cell"><div class="label"><span>Channel 4</span><span class="st" id="s4"></span></div><img id="c4" alt="ch4"/></div>
  </div>
<script>
(function () {
  // One channel at a time — RTSP grabs take 1–5s each; firing all four every
  // 2s starved the frames lock and returned 503 JSON into <img> tags.
  const ids = [1, 2, 3, 4];
  let i = 0;
  function loadOne(n) {
    var el = document.getElementById('c' + n);
    var st = document.getElementById('s' + n);
    if (!el) return;
    if (st) st.textContent = '…';
    var img = new Image();
    img.onload = function () {
      el.src = img.src;
      if (st) st.textContent = new Date().toLocaleTimeString();
    };
    img.onerror = function () {
      if (st) st.textContent = 'retry';
    };
    img.src = '/aeyes/live/ch' + n + '.jpg?t=' + Date.now();
  }
  function tick() {
    loadOne(ids[i % ids.length]);
    i += 1;
  }
  // Initial pass: stagger so all four fill within ~6s without overlapping.
  ids.forEach(function (n, idx) { setTimeout(function () { loadOne(n); }, idx * 1500); });
  setInterval(tick, 4000);
})();
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    server_version = "AEyesCamServer/2.1"

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _json(self, code: int, body: dict) -> None:
        raw = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _html(self, code: int, body: str, *, extra_headers: list[tuple[str, str]] | None = None) -> None:
        raw = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        if extra_headers:
            for k, v in extra_headers:
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    def _jpeg(self, data: bytes) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "image/jpeg")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _cookies(self) -> SimpleCookie:
        c = SimpleCookie()
        raw = self.headers.get("Cookie")
        if raw:
            c.load(raw)
        return c

    def _authed(self) -> bool:
        try:
            expected = _expected_token()
        except (FileNotFoundError, KeyError):
            return False
        morsel = self._cookies().get(COOKIE_NAME)
        if not morsel:
            return False
        return hmac.compare_digest(morsel.value, expected)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path in ("/health", ""):
            self._json(200, {"ok": True, "service": "a-eyes-cam-server"})
            return

        name = path.lstrip("/")
        if name in STILL_ROUTES:
            self._still(STILL_ROUTES[name], require_auth=False)
            return

        if path in ("/aeyes",):
            if self._authed():
                self._html(200, LIVE_HTML)
            else:
                self._html(200, LOGIN_HTML.replace("__ERR__", ""))
            return

        if path == "/aeyes/logout":
            self._html(
                302,
                "",
                extra_headers=[
                    ("Location", "/aeyes"),
                    ("Set-Cookie", f"{COOKIE_NAME}=; Path=/aeyes; Max-Age=0; HttpOnly; SameSite=Lax"),
                ],
            )
            return

        if path.startswith("/aeyes/live/ch") and path.endswith(".jpg"):
            if not self._authed():
                self._json(401, {"ok": False, "error": "unauthorized"})
                return
            try:
                ch = int(path.split("/ch")[-1].split(".")[0])
            except ValueError:
                self._json(404, {"ok": False, "error": "not_found"})
                return
            if ch not in (1, 2, 3, 4):
                self._json(404, {"ok": False, "error": "not_found"})
                return
            self._still(ch, require_auth=False)  # already checked
            return

        self._json(404, {"ok": False, "error": "not_found"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        if path != "/aeyes/login":
            self._json(404, {"ok": False, "error": "not_found"})
            return

        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length > 0 else b""
        form = parse_qs(raw.decode("utf-8", errors="replace"))
        submitted = (form.get("password") or [""])[0]

        try:
            expected_pw = _password()
        except (FileNotFoundError, KeyError) as e:
            self._html(
                500,
                LOGIN_HTML.replace(
                    "__ERR__",
                    f'<div class="err">Server misconfigured: {e}</div>',
                ),
            )
            return

        if not hmac.compare_digest(submitted, expected_pw):
            self._html(
                401,
                LOGIN_HTML.replace("__ERR__", '<div class="err">Wrong password.</div>'),
            )
            return

        token = _session_token(expected_pw)
        self._html(
            302,
            "",
            extra_headers=[
                ("Location", "/aeyes"),
                (
                    "Set-Cookie",
                    f"{COOKIE_NAME}={token}; Path=/aeyes; Max-Age={COOKIE_MAX_AGE}; HttpOnly; SameSite=Lax",
                ),
            ],
        )

    def _still(self, channel: int, *, require_auth: bool = False) -> None:
        if require_auth and not self._authed():
            self._json(401, {"ok": False, "error": "unauthorized"})
            return

        data: bytes | None = None
        try:
            path = grab_jpeg(channel=channel)
            data = path.read_bytes()
            if data and len(data) > 500:
                with _last_lock:
                    _last_jpeg[channel] = data
        except FramesBusy:
            data = None
        except Exception:
            data = None

        if not data:
            with _last_lock:
                data = _last_jpeg.get(channel)
        if not data:
            data = _disk_latest(channel)
            if data:
                with _last_lock:
                    _last_jpeg[channel] = data

        if data:
            self._jpeg(data)
            return

        # Nothing to show yet — still return a tiny valid JPEG-ish failure as JSON
        # only for non-img clients; for live UI we prefer empty 1x1 so <img> doesn't
        # spam broken-icon. Use a minimal 1x1 black JPEG.
        # 1x1 black JPEG:
        tiny = bytes([
            0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01,
            0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xFF, 0xDB, 0x00, 0x43,
            0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07, 0x07, 0x09,
            0x09, 0x08, 0x0A, 0x0C, 0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12,
            0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20,
            0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29,
            0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 0x3D, 0x38, 0x32,
            0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xC0, 0x00, 0x0B, 0x08, 0x00, 0x01,
            0x00, 0x01, 0x01, 0x01, 0x11, 0x00, 0xFF, 0xC4, 0x00, 0x14, 0x00, 0x01,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x08, 0xFF, 0xC4, 0x00, 0x14, 0x10, 0x01, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0xFF, 0xDA, 0x00, 0x08, 0x01, 0x01, 0x00, 0x00, 0x3F, 0x00,
            0x7F, 0xFF, 0xD9,
        ])
        self._jpeg(tiny)


def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"a-eyes cam server listen={HOST}:{PORT}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
