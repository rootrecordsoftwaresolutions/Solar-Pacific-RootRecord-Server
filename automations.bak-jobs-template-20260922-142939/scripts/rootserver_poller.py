#!/usr/bin/env python3
"""RootRecord automations poller — Cloudflare tunnel first, then heartbeat.

Order:
  1) start cloudflared (token tunnel)
  2) wait until at least one tunnel connection registers (or timeout)
  3) bind HTTP + start 5s \"Poller is online.\" loop

Serves the same line on HTTP (open access on the bound port).
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

INTERVAL_SEC = float(os.environ.get("POLLER_INTERVAL_SEC", "5"))
HOST = os.environ.get("POLLER_BIND", "127.0.0.1")
PORT = int(os.environ.get("POLLER_PORT", "8799"))
HOSTNAME = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
TOKEN_FILE = Path(
    os.environ.get(
        "CLOUDFLARED_TOKEN_FILE",
        str(Path.home() / ".cloudflared" / "rootserver.token"),
    )
)
CLOUDFLARED_BIN = os.environ.get(
    "CLOUDFLARED_BIN",
    str(Path(__file__).resolve().parents[1] / "bin" / "cloudflared"),
)
ENABLE_TUNNEL = os.environ.get("POLLER_ENABLE_TUNNEL", "1") != "0"
TUNNEL_READY_TIMEOUT_SEC = float(os.environ.get("POLLER_TUNNEL_READY_TIMEOUT_SEC", "45"))

_latest = "starting"
_lock = threading.Lock()
_stop = threading.Event()
_tunnel_ready = threading.Event()
_tunnel_proc: subprocess.Popen | None = None


def full_timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def heartbeat_line() -> str:
    return f"{full_timestamp()}Poller is online."


def log(msg: str) -> None:
    print(msg, flush=True)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
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
            import json

            self._send(
                200,
                json.dumps({"ok": True, "host": HOSTNAME, "line": line}) + "\n",
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


def start_tunnel() -> bool:
    """Spawn cloudflared. Returns True if spawn started (not necessarily ready)."""
    global _tunnel_proc
    if not ENABLE_TUNNEL:
        log(f"{full_timestamp()}Tunnel disabled (POLLER_ENABLE_TUNNEL=0).")
        _tunnel_ready.set()
        return False
    if not Path(CLOUDFLARED_BIN).is_file():
        log(f"{full_timestamp()}Tunnel DOWN — cloudflared missing at {CLOUDFLARED_BIN}")
        return False
    if not TOKEN_FILE.is_file():
        log(f"{full_timestamp()}Tunnel DOWN — token file missing: {TOKEN_FILE}")
        return False
    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not token:
        log(f"{full_timestamp()}Tunnel DOWN — empty token file")
        return False

    mode = os.environ.get("POLLER_TUNNEL_MODE", "token").lower()
    if mode == "quick":
        cmd = [
            CLOUDFLARED_BIN,
            "tunnel",
            "--no-autoupdate",
            "--url",
            f"http://{HOST}:{PORT}",
        ]
        popen_kwargs: dict = {}
    else:
        cmd = [
            CLOUDFLARED_BIN,
            "tunnel",
            "--no-autoupdate",
            "run",
        ]
        env = os.environ.copy()
        env["TUNNEL_TOKEN"] = token
        popen_kwargs = {"env": env}

    log(f"{full_timestamp()}Starting cloudflared mode={mode} public_host={HOSTNAME}")
    _tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        **popen_kwargs,
    )

    def _cloudflared_interesting(text: str) -> str | None:
        """Return a short line to log, or None to drop noise."""
        t = text.strip()
        if not t:
            return None
        # Drop precheck banners / tables / component spam
        drop_sub = (
            "CONNECTIVITY PRE-CHECKS",
            "-----------",
            "COMPONENT         TARGET",
            "precheck component=",
            "precheck complete",
            "SUMMARY:",
            "DNS Resolution",
            "UDP Connectivity",
            "TCP Connectivity",
            "Cloudflare API",
            "Tunnel connection curve preferences",
            "ICMP proxy will use",
            "Generated Connector ID",
            "Initial protocol",
            "Starting metrics server",
            "Version ",
            "GOOS:",
            "Settings: map[",
            "Environmental variables map[",
            "Autoupdate frequency",
            "Metrics server",
        )
        if any(s in t for s in drop_sub):
            return None
        if t.startswith("|") or t.startswith("+--"):
            return None
        # Keep errors/warns and useful lifecycle
        low = t.lower()
        if " err " in f" {low} " or "error" in low or "failed" in low or " warn" in low:
            return f"cloudflared ERR/WARN: {t}"
        if "Registered tunnel connection" in t:
            # connIndex=0 location=sjc08 protocol=quic
            idx = ""
            loc = ""
            for part in t.split():
                if part.startswith("connIndex="):
                    idx = part.split("=", 1)[1]
                if part.startswith("location="):
                    loc = part.split("=", 1)[1]
            return f"tunnel connected  conn={idx or '?'}  edge={loc or '?'}"
        if "Starting tunnel" in t:
            tid = ""
            for part in t.split():
                if part.startswith("tunnelID="):
                    tid = part.split("=", 1)[1]
            return f"tunnel starting  id={tid or '?'}"
        if "Updated to new configuration" in t:
            if "rootserver.rootrecord.cloud" in t:
                return "tunnel ingress  rootserver.rootrecord.cloud → 127.0.0.1:8799"
            return "tunnel ingress  updated"
        if "Connected to Cloudflare" in t:
            return "tunnel connected to Cloudflare"
        return None  # default: quiet

    def pump() -> None:
        assert _tunnel_proc is not None
        assert _tunnel_proc.stdout is not None
        for line in _tunnel_proc.stdout:
            text = line.rstrip()
            interesting = _cloudflared_interesting(text)
            if interesting:
                log(f"{full_timestamp()}{interesting}")
            # First registered connection = tunnel path is live enough to poll.
            if "Registered tunnel connection" in text or "Connected to Cloudflare" in text:
                if not _tunnel_ready.is_set():
                    log(f"{full_timestamp()}Tunnel READY — first connection registered.")
                    _tunnel_ready.set()
            if _stop.is_set():
                break
        if _tunnel_proc.poll() is not None and not _tunnel_ready.is_set():
            log(f"{full_timestamp()}Tunnel DOWN — cloudflared exited before ready (code={_tunnel_proc.returncode}).")

    threading.Thread(target=pump, name="cloudflared-log", daemon=True).start()
    return True


def wait_for_tunnel_ready() -> None:
    if not ENABLE_TUNNEL:
        return
    if _tunnel_ready.is_set():
        return
    log(
        f"{full_timestamp()}Waiting for tunnel register "
        f"(timeout={TUNNEL_READY_TIMEOUT_SEC:.0f}s) before polling…"
    )
    if _tunnel_ready.wait(timeout=TUNNEL_READY_TIMEOUT_SEC):
        return
    log(
        f"{full_timestamp()}Tunnel WAITING — no register within "
        f"{TUNNEL_READY_TIMEOUT_SEC:.0f}s; starting poller anyway."
    )


def shutdown(*_args) -> None:
    _stop.set()
    _tunnel_ready.set()
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

    # 1) Tunnel first — before HTTP bind and before heartbeat polling.
    started = start_tunnel()
    if started:
        wait_for_tunnel_ready()
    elif ENABLE_TUNNEL:
        log(f"{full_timestamp()}Tunnel DOWN — continuing with local poller only.")

    # 2) Local HTTP, then 3) heartbeat loop.
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    threading.Thread(target=server.serve_forever, name="http", daemon=True).start()
    log(f"{full_timestamp()}HTTP listening on http://{HOST}:{PORT} (open access on bind)")

    heartbeat_loop()

    server.shutdown()
    shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
