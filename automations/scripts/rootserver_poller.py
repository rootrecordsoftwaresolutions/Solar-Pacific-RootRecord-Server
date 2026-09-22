#!/usr/bin/env python3
"""RootRecord automations poller — heartbeat + optional Cloudflare tunnel.

Every 5 seconds logs: <FULLTIMESTAMP>Poller is online.
Serves the same line on HTTP (open access on the bound port).
Optional: spawn cloudflared with a tunnel token to publish that port.
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

INTERVAL_SEC = float(os.environ.get("POLLER_INTERVAL_SEC", "5"))
HOST = os.environ.get("POLLER_BIND", "127.0.0.1")
PORT = int(os.environ.get("POLLER_PORT", "8799"))
HOSTNAME = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
TOKEN_FILE = Path(
    os.environ.get(
        "CLOUDFLARED_TOKEN_FILE",
        str(Path.home() / ".cloudflared" / "origin.token"),
    )
)
CLOUDFLARED_BIN = os.environ.get(
    "CLOUDFLARED_BIN",
    str(Path(__file__).resolve().parents[1] / "bin" / "cloudflared"),
)
ENABLE_TUNNEL = os.environ.get("POLLER_ENABLE_TUNNEL", "1") != "0"

_latest = "starting"
_lock = threading.Lock()
_stop = threading.Event()
_tunnel_proc: subprocess.Popen | None = None


def full_timestamp() -> str:
    # Full ISO-8601 with timezone offset (HST on this host when TZ is local)
    return datetime.now().astimezone().isoformat(timespec="seconds")


def heartbeat_line() -> str:
    return f"{full_timestamp()}Poller is online."


def log(msg: str) -> None:
    print(msg, flush=True)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:  # quieter access log
        return

    def _send(self, code: int, body: str, ctype: str = "text/plain; charset=utf-8") -> None:
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        with _lock:
            line = _latest
        if self.path in ("/", "/health", "/poller"):
            self._send(200, line + "\n")
            return
        if self.path == "/json":
            self._send(
                200,
                (
                    '{"ok":true,"host":%s,"line":%s}\n'
                    % (
                        __import__("json").dumps(HOSTNAME),
                        __import__("json").dumps(line),
                    )
                ),
                "application/json; charset=utf-8",
            )
            return
        self._send(404, "not found\n")


def heartbeat_loop() -> None:
    global _latest
    while not _stop.is_set():
        line = heartbeat_line()
        with _lock:
            _latest = line
        log(line)
        _stop.wait(INTERVAL_SEC)


def start_tunnel() -> None:
    global _tunnel_proc
    if not ENABLE_TUNNEL:
        log(f"{full_timestamp()}Tunnel disabled (POLLER_ENABLE_TUNNEL=0).")
        return
    if not Path(CLOUDFLARED_BIN).is_file():
        log(f"{full_timestamp()}Tunnel DOWN — cloudflared missing at {CLOUDFLARED_BIN}")
        return
    if not TOKEN_FILE.is_file():
        log(f"{full_timestamp()}Tunnel DOWN — token file missing: {TOKEN_FILE}")
        return
    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not token:
        log(f"{full_timestamp()}Tunnel DOWN — empty token file")
        return
    # Token tunnels get hostname/ingress from Cloudflare Zero Trust config.
    # Local side only needs: run --token <token> (ingress already points at a service URL).
    # We also support quick mode via POLLER_TUNNEL_MODE=quick (ephemeral URL, not the named host).
    mode = os.environ.get("POLLER_TUNNEL_MODE", "token").lower()
    if mode == "quick":
        cmd = [
            CLOUDFLARED_BIN,
            "tunnel",
            "--no-autoupdate",
            "--url",
            f"http://{HOST}:{PORT}",
        ]
    else:
        cmd = [
            CLOUDFLARED_BIN,
            "tunnel",
            "--no-autoupdate",
            "run",
        ]
        # Token via env — never put on argv (shows in ps).
        env = os.environ.copy()
        env["TUNNEL_TOKEN"] = token
    log(f"{full_timestamp()}Starting cloudflared mode={mode} public_host={HOSTNAME}")
    popen_kwargs = dict(
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    if mode != "quick":
        popen_kwargs["env"] = env
    _tunnel_proc = subprocess.Popen(cmd, **popen_kwargs)

    def pump() -> None:
        assert _tunnel_proc is not None
        assert _tunnel_proc.stdout is not None
        for line in _tunnel_proc.stdout:
            log(f"{full_timestamp()}cloudflared: {line.rstrip()}")
            if _stop.is_set():
                break

    threading.Thread(target=pump, name="cloudflared-log", daemon=True).start()


def shutdown(*_args) -> None:
    _stop.set()
    global _tunnel_proc
    if _tunnel_proc and _tunnel_proc.poll() is None:
        _tunnel_proc.terminate()
        try:
            _tunnel_proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            _tunnel_proc.kill()


def main() -> int:
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    server = ThreadingHTTPServer((HOST, PORT), Handler)
    threading.Thread(target=server.serve_forever, name="http", daemon=True).start()
    log(f"{full_timestamp()}HTTP listening on http://{HOST}:{PORT} (open access on bind)")

    start_tunnel()
    heartbeat_loop()

    server.shutdown()
    shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
