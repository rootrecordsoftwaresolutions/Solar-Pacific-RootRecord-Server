#!/usr/bin/env python3
"""a-eyes light gateway: health + current.jpg from Night Owl RTSP."""
from __future__ import annotations
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from panels_grab import grab_jpeg  # noqa: E402

SKILL = ROOT.parent
SECRETS = SKILL / "store" / "secrets.env"
STATE = SKILL / "store" / "gateway-state.json"


def _load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if SECRETS.is_file():
        for line in SECRETS.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("RR_SOLAR_PATH_SECRET", "RR_SOLAR_LISTEN", "RR_SOLAR_CHANNEL"):
        if os.environ.get(k):
            env[k] = os.environ[k].strip()
    return env


class Handler(BaseHTTPRequestHandler):
    server_version = "AEyesGateway/1.0"

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _secret(self) -> str:
        return str(getattr(self.server, "path_secret", "") or "")

    def _json(self, code: int, body: dict) -> None:
        raw = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _deny(self) -> None:
        self._json(404, {"ok": False, "error": "not_found"})

    def _rest(self) -> str | None:
        path = urlparse(self.path).path
        secret = self._secret().strip("/")
        if not secret:
            # no secret configured → allow /health and /current.jpg at root
            return path.lstrip("/") or "health"
        pref = "/" + secret
        if path != pref and not path.startswith(pref + "/"):
            return None
        return path[len(pref):].lstrip("/") or "health"

    def do_GET(self) -> None:
        rest = self._rest()
        if rest is None:
            self._deny()
            return
        if rest == "health":
            self._json(200, {"ok": True, "service": "a-eyes-gateway"})
            return
        if rest in ("current.jpg", "still.jpg"):
            self._still()
            return
        self._deny()

    def _still(self) -> None:
        env = _load_env()
        ch = int(env.get("RR_SOLAR_CHANNEL") or 1)
        try:
            path = grab_jpeg(channel=ch, stream=0)
            data = path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            STATE.parent.mkdir(parents=True, exist_ok=True)
            STATE.write_text(json.dumps({"ok": True, "path": str(path), "ch": ch}) + "\n")
        except Exception as e:
            self._json(503, {"ok": False, "error": str(e)[:300]})


def main() -> None:
    env = _load_env()
    listen = env.get("RR_SOLAR_LISTEN") or "127.0.0.1:8791"
    host, _, port_s = listen.partition(":")
    host = host or "127.0.0.1"
    port = int(port_s or "8791")
    secret = env.get("RR_SOLAR_PATH_SECRET") or ""
    httpd = ThreadingHTTPServer((host, port), Handler)
    httpd.path_secret = secret  # type: ignore[attr-defined]
    print(f"a-eyes gateway listen={host}:{port} secret={'set' if secret else 'none'}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
