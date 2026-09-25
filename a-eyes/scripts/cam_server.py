#!/usr/bin/env python3
"""a-eyes local camera server.

Broadcasts on LOCALHOST ONLY (127.0.0.1) by default. This is the one and
only server that should be hosting camera views for this skill. If you
find another process bound to a camera/gateway port on this box, it's a
leftover from the old setup and should be killed.

Routes:
  GET /health           -> {"ok": true}
  GET /current.jpg      -> channel 1 still
  GET /current_ch2.jpg  -> channel 2 still
  GET /current_ch3.jpg  -> channel 3 still
  GET /current_ch4.jpg  -> channel 4 still
"""
from __future__ import annotations
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from grab_frame import grab_jpeg  # noqa: E402

HOST = "127.0.0.1"
PORT = 8791

ROUTES = {
    "current.jpg": 1,
    "current_ch2.jpg": 2,
    "current_ch3.jpg": 3,
    "current_ch4.jpg": 4,
}


class Handler(BaseHTTPRequestHandler):
    server_version = "AEyesCamServer/1.0"

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _json(self, code: int, body: dict) -> None:
        import json
        raw = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        rest = urlparse(self.path).path.lstrip("/")
        if rest in ("", "health"):
            self._json(200, {"ok": True, "service": "a-eyes-cam-server"})
            return
        if rest in ROUTES:
            self._still(ROUTES[rest])
            return
        self._json(404, {"ok": False, "error": "not_found"})

    def _still(self, channel: int) -> None:
        try:
            path = grab_jpeg(channel=channel)
            data = path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self._json(503, {"ok": False, "error": f"Ch{channel} failed: {str(e)[:250]}"})


def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"a-eyes cam server listen={HOST}:{PORT}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
