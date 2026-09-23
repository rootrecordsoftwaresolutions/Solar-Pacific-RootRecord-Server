#!/usr/bin/env python3
"""RootRecord automations poller — tunnel first, then scheduled jobs.

# INFO — MUST HAVE (future agents):
# Ctrl-C / stop-poller-stack.sh must terminate this process, cloudflared, and
# rr-rootserver-poller.service. See scripts/jobs.py header and stop-poller-stack.sh.
#
# Job definitions live in jobs.py — ON_BOOT priorities (0=self, 1=cloudflare, 2+=templates),
# then recurring sections. Keep section formatting identical.
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

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import jobs as jobmod  # noqa: E402

INTERVAL_FALLBACK = float(os.environ.get("POLLER_INTERVAL_SEC", "5"))
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
    str(SCRIPTS.parent / "bin" / "cloudflared"),
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


def log(msg: str) -> None:
    print(msg, flush=True)


def heartbeat_line() -> str:
    return f"{full_timestamp()}Poller is online."


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


def _cloudflared_interesting(text: str) -> str | None:
    t = text.strip()
    if not t:
        return None
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
    low = t.lower()
    if " err " in f" {low} " or t.startswith("ERR") or "error=" in low:
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        if "terminated" in low:
            return "tunnel connection terminated"
        return f"cloudflared ERR: {t[:160]}"
    if t.startswith("WRN") or " WRN " in f" {t} ":
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        return f"cloudflared WRN: {t[:160]}"
    if "Registered tunnel connection" in t:
        idx = loc = ""
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
    return None


def start_tunnel() -> bool:
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
        cmd = [CLOUDFLARED_BIN, "tunnel", "--no-autoupdate", "--url", f"http://{HOST}:{PORT}"]
        popen_kwargs: dict = {}
    else:
        cmd = [CLOUDFLARED_BIN, "tunnel", "--no-autoupdate", "run"]
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

    def pump() -> None:
        assert _tunnel_proc is not None and _tunnel_proc.stdout is not None
        for line in _tunnel_proc.stdout:
            text = line.rstrip()
            interesting = _cloudflared_interesting(text)
            if interesting:
                log(f"{full_timestamp()}{interesting}")
            if "Registered tunnel connection" in text or "Connected to Cloudflare" in text:
                if not _tunnel_ready.is_set():
                    log(f"{full_timestamp()}Tunnel READY — first connection registered.")
                    _tunnel_ready.set()
            if _stop.is_set():
                break
        if _tunnel_proc.poll() is not None and not _tunnel_ready.is_set():
            log(
                f"{full_timestamp()}Tunnel DOWN — cloudflared exited before ready "
                f"(code={_tunnel_proc.returncode})."
            )

    threading.Thread(target=pump, name="cloudflared-log", daemon=True).start()
    return True


def wait_for_tunnel_ready() -> None:
    if not ENABLE_TUNNEL or _tunnel_ready.is_set():
        return
    log(
        f"{full_timestamp()}Waiting for tunnel register "
        f"(timeout={TUNNEL_READY_TIMEOUT_SEC:.0f}s) before jobs…"
    )
    if not _tunnel_ready.wait(timeout=TUNNEL_READY_TIMEOUT_SEC):
        log(
            f"{full_timestamp()}Tunnel WAITING — no register within "
            f"{TUNNEL_READY_TIMEOUT_SEC:.0f}s; starting jobs anyway."
        )


def run_command_job(job: dict) -> None:
    jid = job.get("id", "?")
    cmd = (job.get("command") or "").strip()
    if not cmd:
        log(f"{full_timestamp()}job:{jid} SKIP — empty command")
        return
    timeout = float(job.get("timeout_sec") or 120)
    cwd = (job.get("cwd") or "").strip() or None
    env = os.environ.copy()
    extra = job.get("env") or {}
    if isinstance(extra, dict):
        env.update({str(k): str(v) for k, v in extra.items()})
    quiet = jid in ("github_sync_all", "github_setup_remotes", "github_autopush")
    if not quiet:
        log(f"{full_timestamp()}job:{jid} RUN  {cmd}")
    try:
        r = subprocess.run(
            ["bash", "-lc", cmd],
            cwd=cwd,
            env=env,
            timeout=timeout,
            capture_output=True,
            text=True,
        )
        out = (r.stdout or "").strip()
        err = (r.stderr or "").strip()
        if r.returncode == 0:
            if out:
                for line in out.splitlines()[:40]:
                    line = line.strip()
                    if not line:
                        continue
                    # Drop noisy setup chatter; keep sync results.
                    if quiet and any(
                        line.startswith(p)
                        for p in ("[ok]", "[skip]", "[clone]", "Updated", "Added", "Done.")
                    ):
                        continue
                    log(f"{full_timestamp()}job:{jid} | {line}")
            elif not quiet:
                log(f"{full_timestamp()}job:{jid} OK")
        else:
            log(f"{full_timestamp()}job:{jid} FAIL code={r.returncode}")
            for line in (err or out).splitlines()[:20]:
                log(f"{full_timestamp()}job:{jid} ! {line}")
    except subprocess.TimeoutExpired:
        log(f"{full_timestamp()}job:{jid} TIMEOUT after {timeout:.0f}s")
    except Exception as e:
        log(f"{full_timestamp()}job:{jid} ERROR {e}")


def run_builtin(job: dict) -> None:
    global _latest
    jid = job.get("id", "?")
    name = (job.get("builtin") or "").strip()
    if name == "heartbeat":
        line = heartbeat_line()
        with _lock:
            _latest = line
        log(line)
        return
    if name == "self_process":
        # Priority 0 boot registry — lists this desk + status terminal.
        proc = job.get("process") or str(Path(__file__).resolve())
        term = job.get("terminal") or "RootRecord poller — rootserver"
        watch = job.get("watch") or str(SCRIPTS / "poller-watch.py")
        log(f"{full_timestamp()}boot:p0 self_process")
        log(f"{full_timestamp()}boot:p0 process  = {proc}")
        log(f"{full_timestamp()}boot:p0 terminal = {term}")
        log(f"{full_timestamp()}boot:p0 watch    = {watch}")
        log(f"{full_timestamp()}boot:p0 pid      = {os.getpid()}")
        return
    if name == "tunnel_start":
        # Priority 1 boot — Cloudflare tunnel (was hard-coded; now job-driven).
        global HOSTNAME, TOKEN_FILE, CLOUDFLARED_BIN, TUNNEL_READY_TIMEOUT_SEC
        if job.get("public_host"):
            HOSTNAME = str(job["public_host"])
        if job.get("token_file"):
            TOKEN_FILE = Path(str(job["token_file"]))
        if job.get("cloudflared_bin"):
            CLOUDFLARED_BIN = str(job["cloudflared_bin"])
        if job.get("timeout_sec"):
            TUNNEL_READY_TIMEOUT_SEC = float(job["timeout_sec"])
        log(f"{full_timestamp()}boot:p1 cloudflare_tunnel host={HOSTNAME}")
        started = start_tunnel()
        if started:
            wait_for_tunnel_ready()
        elif ENABLE_TUNNEL:
            log(f"{full_timestamp()}Tunnel DOWN — continuing with local jobs only.")
        return
    if name == "http_ping":
        url = (job.get("command") or f"http://{HOST}:{PORT}/").strip()
        try:
            import urllib.request

            with urllib.request.urlopen(url, timeout=5) as resp:
                log(f"{full_timestamp()}job:{jid} http_ping {resp.status} {url}")
        except Exception as e:
            log(f"{full_timestamp()}job:{jid} http_ping FAIL {e}")
        return
    log(f"{full_timestamp()}job:{jid} UNKNOWN builtin={name!r}")


def run_job(job: dict) -> None:
    if not job.get("enabled"):
        return
    builtin = (job.get("builtin") or "").strip()
    if builtin:
        run_builtin(job)
        return
    run_command_job(job)


def enabled_jobs(section: list) -> list:
    return [j for j in section if isinstance(j, dict) and j.get("enabled")]


def scheduler_loop() -> None:
    """Drive EVERY_SECONDS / EVERY_MINUTE / EVERY_HOUR until stop."""
    sec_jobs = enabled_jobs(getattr(jobmod, "EVERY_SECONDS", []))
    min_jobs = enabled_jobs(getattr(jobmod, "EVERY_MINUTE", []))
    hour_jobs = enabled_jobs(getattr(jobmod, "EVERY_HOUR", []))

    next_due: dict[str, float] = {}
    now = time.monotonic()
    for j in sec_jobs:
        interval = float(j.get("interval_sec") or INTERVAL_FALLBACK)
        if interval <= 0:
            interval = INTERVAL_FALLBACK
        # fire soon after start
        next_due[j["id"]] = now

    last_minute: int | None = None
    last_hour: int | None = None

    log(
        f"{full_timestamp()}scheduler  "
        f"every_seconds={len(sec_jobs)}  every_minute={len(min_jobs)}  "
        f"every_hour={len(hour_jobs)}"
    )

    while not _stop.is_set():
        wall = datetime.now().astimezone()
        mono = time.monotonic()

        for j in sec_jobs:
            jid = j["id"]
            if mono >= next_due.get(jid, 0):
                run_job(j)
                interval = float(j.get("interval_sec") or INTERVAL_FALLBACK)
                next_due[jid] = mono + max(0.2, interval)

        minute = wall.minute
        hour = wall.hour
        if last_minute is None:
            last_minute = minute
            last_hour = hour
        else:
            if minute != last_minute:
                for j in min_jobs:
                    only = j.get("only_at_minutes") or []
                    if only and minute not in only:
                        continue
                    run_job(j)
                last_minute = minute
            if hour != last_hour and minute == 0:
                for j in hour_jobs:
                    only = j.get("only_at_hours") or []
                    if only and hour not in only:
                        continue
                    run_job(j)
                last_hour = hour
            elif hour != last_hour:
                last_hour = hour

        _stop.wait(0.25)


def shutdown(*_args) -> None:
    """INFO — MUST HAVE: tear down tunnel child with this process."""
    _stop.set()
    _tunnel_ready.set()
    global _tunnel_proc
    if _tunnel_proc and _tunnel_proc.poll() is None:
        _tunnel_proc.terminate()
        try:
            _tunnel_proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            _tunnel_proc.kill()


def run_on_boot() -> None:
    """ON_BOOT priority list — lower priority number runs first."""
    boot = [j for j in enabled_jobs(getattr(jobmod, "ON_BOOT", [])) if isinstance(j, dict)]
    boot.sort(key=lambda j: int(j.get("priority", 100)))
    log(f"{full_timestamp()}boot:start  jobs={len(boot)}")
    for j in boot:
        prio = j.get("priority", "?")
        jid = j.get("id", "?")
        log(f"{full_timestamp()}boot:run  priority={prio}  id={jid}")
        run_job(j)
    log(f"{full_timestamp()}boot:done")


def main() -> int:
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    # HTTP bind early so local health works even while tunnel is coming up.
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    threading.Thread(target=server.serve_forever, name="http", daemon=True).start()
    log(f"{full_timestamp()}HTTP listening on http://{HOST}:{PORT} (open access on bind)")

    # Boot priority chain: p0 self_terminal → p1 cloudflare → p2+ templates
    run_on_boot()

    for j in enabled_jobs(getattr(jobmod, "ONCE_AT_START", [])):
        run_job(j)

    scheduler_loop()

    server.shutdown()
    shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
