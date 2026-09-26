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
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from grab_frame import FramesBusy, grab_jpeg, load_master_key  # noqa: E402

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


def _password() -> str:
    return load_master_key("AEYES_PUBLIC_PASSWORD")


def _session_token(password: str) -> str:
    # Stable token derived from password; no server-side session store needed.
    return hmac.new(
        b"aeyes-public-v1",
        password.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def _expected_token() -> str:
    return _session_token(_password())


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
           border-bottom: 1px solid #1c2533; }
  .cell img { display: block; width: 100%; height: auto; background: #000; min-height: 120px; }
</style>
</head>
<body>
  <header>
    <h1>a-eyes — live</h1>
    <a href="/aeyes/logout">Log out</a>
  </header>
  <div class="grid">
    <div class="cell"><div class="label">Channel 1</div><img id="c1" alt="ch1"/></div>
    <div class="cell"><div class="label">Channel 2</div><img id="c2" alt="ch2"/></div>
    <div class="cell"><div class="label">Channel 3</div><img id="c3" alt="ch3"/></div>
    <div class="cell"><div class="label">Channel 4</div><img id="c4" alt="ch4"/></div>
  </div>
<script>
(function () {
  const ids = [1, 2, 3, 4];
  function tick() {
    const t = Date.now();
    ids.forEach(function (n) {
      var el = document.getElementById('c' + n);
      if (el) el.src = '/aeyes/live/ch' + n + '.jpg?t=' + t;
    });
  }
  tick();
  setInterval(tick, 2000);
})();
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    server_version = "AEyesCamServer/2.0"

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

        # Legacy still routes (local only / optional auth not required on LAN)
        name = path.lstrip("/")
        if name in STILL_ROUTES:
            self._still(STILL_ROUTES[name])
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
            self._still(ch)
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

    def _still(self, channel: int) -> None:
        try:
            path = grab_jpeg(channel=channel)
            data = path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
        except FramesBusy:
            self._json(503, {"ok": False, "error": f"Ch{channel} busy — try again"})
        except Exception as e:
            self._json(503, {"ok": False, "error": f"Ch{channel} failed: {str(e)[:250]}"})


def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"a-eyes cam server listen={HOST}:{PORT}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
