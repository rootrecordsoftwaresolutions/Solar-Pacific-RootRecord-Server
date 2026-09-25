#!/usr/bin/env python3
"""Pretty live view of the rootserver poller log (colors + filter).

# INFO — MUST HAVE (future agents):
# Ctrl-C OR closing this window MUST stop the entire stack (poller, cloudflared,
# systemd unit). Never exit the window while leaving those processes up.
"""
from __future__ import annotations

import atexit
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
STOP = SCRIPTS / "stop-poller-stack.sh"
LOG = Path(
    os.environ.get(
        "POLLER_LOG",
        str(Path.home() / ".ollama/skills/logs/store/rootserver-poller.log"),
    )
)
HOST = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
LOCAL = os.environ.get("POLLER_LOCAL", "http://127.0.0.1:8799/")

RST = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"
WHITE = "\033[97m"

_stop_done = False


def unit_state() -> str:
    try:
        r = subprocess.run(
            ["systemctl", "--user", "is-active", "rr-rootserver-poller.service"],
            capture_output=True,
            text=True,
            timeout=3,
        )
        return (r.stdout or r.stderr or "unknown").strip()
    except Exception:
        return "unknown"


def stop_everything(reason: str = "exit") -> None:
    """Idempotent full stack stop. Called on Ctrl-C, window close, or signals."""
    global _stop_done
    if _stop_done:
        return
    _stop_done = True
    try:
        print(
            f"\n{YELLOW}{reason} — stopping ENTIRE stack "
            f"(poller + tunnel + unit)…{RST}",
            flush=True,
        )
    except Exception:
        pass
    try:
        subprocess.run(["bash", str(STOP)], check=False, timeout=60)
    except Exception as e:
        try:
            print(f"{RED}stop failed: {e}{RST}", flush=True)
        except Exception:
            pass
    try:
        print(f"{DIM}stack stop requested — window exiting{RST}", flush=True)
    except Exception:
        pass


def _on_signal(signum: int, _frame) -> None:
    names = {
        signal.SIGINT: "Ctrl-C",
        signal.SIGTERM: "SIGTERM",
        signal.SIGHUP: "window close (SIGHUP)",
    }
    reason = names.get(signum, f"signal {signum}")
    stop_everything(reason)
    # Exit cleanly after stop so the terminal does not hang
    sys.exit(0)


def _install_handlers() -> None:
    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
        try:
            signal.signal(sig, _on_signal)
        except Exception:
            pass
    # Closing some terminals only triggers atexit / normal exit
    atexit.register(lambda: stop_everything("window exit"))


def banner() -> None:
    state = unit_state()
    if state == "active":
        st = f"{BRIGHT_GREEN}● {state}{RST}"
    elif state in ("activating", "reloading"):
        st = f"{YELLOW}● {state}{RST}"
    else:
        st = f"{RED}● {state}{RST}"
    width = 64
    bar = "─" * (width - 2)
    print(f"{CYAN}{BOLD}╭─ RootRecord poller {bar}{RST}", flush=True)
    print(f"{CYAN}│{RST}  public   {WHITE}https://{HOST}/{RST}", flush=True)
    print(f"{CYAN}│{RST}  local    {DIM}{LOCAL}{RST}", flush=True)
    print(f"{CYAN}│{RST}  systemd  {st}", flush=True)
    print(f"{CYAN}│{RST}  jobs     {DIM}{SCRIPTS / 'jobs.py'}{RST}", flush=True)
    print(f"{CYAN}│{RST}  log      {DIM}{LOG}{RST}", flush=True)
    print(
        f"{CYAN}│{RST}  {YELLOW}Ctrl-C or close window stops EVERY process"
        f" (poller + cloudflared + unit){RST}",
        flush=True,
    )
    print(f"{CYAN}{BOLD}╰{bar}──{RST}", flush=True)
    print(flush=True)


def split_ts(line: str) -> tuple[str, str]:
    if len(line) >= 25 and line[10:11] == "T" and line[19:20] in "+-":
        return line[:25], line[25:]
    return "", line


def clock(ts: str) -> str:
    if "T" in ts and len(ts) >= 19:
        return ts[11:19]
    return ts or "--:--:--"


def _edge_bits(s: str) -> str:
    idx = loc = ""
    for part in s.replace('"', " ").split():
        if part.startswith("connIndex="):
            idx = part.split("=", 1)[1]
        if part.startswith("location="):
            loc = part.split("=", 1)[1]
    bits = []
    if idx:
        bits.append(f"conn={idx}")
    if loc:
        bits.append(f"edge={loc}")
    return "  ".join(bits)


def format_line(raw: str) -> str | None:
    line = raw.rstrip("\n")
    if not line:
        return None
    ts, rest = split_ts(line)
    t = clock(ts)
    body = rest

    noise = (
        "CONNECTIVITY PRE-CHECKS",
        "precheck ",
        "curve preferences",
        "ICMP proxy",
        "Generated Connector",
        "Initial protocol",
        "Starting metrics",
        "Environmental variables",
        "GOOS:",
        "Settings: map",
        "SUMMARY:",
        "DNS Resolution",
        "UDP Connectivity",
        "TCP Connectivity",
        "Cloudflare API",
        "Updated to new configuration",
        "Version ",
    )
    if any(n in body for n in noise) or body.strip().startswith("|") or body.strip().startswith("+--"):
        return None

    if body.startswith("cloudflared: "):
        raw_cf = body[len("cloudflared: ") :]
        if "Registered tunnel connection" in raw_cf:
            bits = _edge_bits(raw_cf)
            return f"  {DIM}{t}{RST}  {CYAN}◆{RST}  {CYAN}tunnel connected{RST}  {DIM}{bits}{RST}"
        if "Starting tunnel" in raw_cf:
            return f"  {DIM}{t}{RST}  {MAGENTA}▲{RST}  {MAGENTA}tunnel starting{RST}"
        if "error=" in raw_cf.lower() or " ERR" in raw_cf or raw_cf.startswith("ERR"):
            short = "tunnel timeout — reconnecting" if "timeout" in raw_cf.lower() else "tunnel error"
            return f"  {DIM}{t}{RST}  {YELLOW}!{RST}  {YELLOW}{short}{RST}"
        if " WRN" in raw_cf or raw_cf.startswith("WRN"):
            short = "tunnel timeout — reconnecting" if "timeout" in raw_cf.lower() else "tunnel warn"
            return f"  {DIM}{t}{RST}  {YELLOW}!{RST}  {YELLOW}{short}{RST}"
        return None

    if body.startswith("Poller is online"):
        return f"  {DIM}{t}{RST}  {BRIGHT_GREEN}●{RST}  {GREEN}Poller is online.{RST}"
    if "Tunnel READY" in body:
        return f"  {DIM}{t}{RST}  {CYAN}◆{RST}  {CYAN}{BOLD}Tunnel READY{RST}{DIM} — registered{RST}"
    if "Tunnel DOWN" in body or "Tunnel WAITING" in body:
        return f"  {DIM}{t}{RST}  {RED}✗{RST}  {RED}{body}{RST}"
    if body.startswith("Waiting for tunnel"):
        return f"  {DIM}{t}{RST}  {YELLOW}…{RST}  {YELLOW}waiting for tunnel…{RST}"
    if body.startswith("Starting cloudflared"):
        return f"  {DIM}{t}{RST}  {MAGENTA}▲{RST}  {MAGENTA}starting cloudflared{RST}"
    if body.startswith("tunnel starting"):
        return f"  {DIM}{t}{RST}  {MAGENTA}▲{RST}  {MAGENTA}{body}{RST}"
    if body.startswith("tunnel connected"):
        return f"  {DIM}{t}{RST}  {CYAN}◆{RST}  {CYAN}{body}{RST}"
    if body.startswith("tunnel ingress"):
        return f"  {DIM}{t}{RST}  {CYAN}→{RST}  {WHITE}{body}{RST}"
    if body.startswith("HTTP listening"):
        return f"  {DIM}{t}{RST}  {WHITE}○{RST}  HTTP listening on :8799"
    if body.startswith("scheduler"):
        return f"  {DIM}{t}{RST}  {WHITE}☰{RST}  {body}"
    if "OK wrote/updated" in body and "worklog" in body.lower():
        short = body if len(body) <= 90 else body[:87] + "…"
        return f"  {DIM}{t}{RST}  {BRIGHT_GREEN}📓{RST}  {GREEN}{short}{RST}"
    if body.startswith("ENERGY "):
        return f"  {DIM}{t}{RST}  {YELLOW}⚡{RST}  {YELLOW}{body}{RST}"
    if body.startswith("SUMMARY=") or body.startswith("STATUS="):
        return f"  {DIM}{t}{RST}  {DIM}▸{RST}  {body}"
    if body.startswith("job:"):
        if " | " in body:
            payload = body.split(" | ", 1)[1].strip()
            repo = ""
            rest = payload
            if "] [" in payload:
                try:
                    after = payload.split("] ", 1)[1]
                    if after.startswith("[") and "]" in after:
                        repo = after[1 : after.index("]")]
                        rest = after[after.index("]") + 1 :].strip()
                except Exception:
                    rest = payload
            # Worklog success — green notebook
            if "worklog" in rest.lower() or "WORKLOG" in rest or "worklog_current" in rest:
                short = rest
                if len(short) > 90:
                    short = short[:87] + "…"
                return f"  {DIM}{t}{RST}  {BRIGHT_GREEN}📓{RST}  {GREEN}{short}{RST}"
            if "no changes" in rest or rest.startswith("—"):
                if repo:
                    return f"  {DIM}{t}{RST}  {DIM}▸{RST}  {DIM}github {repo} · no changes{RST}"
                return None
            if rest.startswith("↑") or " files" in rest or "pushed" in rest.lower():
                n = ""
                for tok in rest.replace("file(s)", "files").split():
                    if tok.isdigit():
                        n = tok
                        break
                label = repo or "repo"
                if n:
                    return f"  {DIM}{t}{RST}  {GREEN}▸{RST}  {GREEN}github {label}{RST}  {DIM}↑ {n} files{RST}"
                return f"  {DIM}{t}{RST}  {GREEN}▸{RST}  {GREEN}github {label}{RST}  {DIM}{rest}{RST}"
            if rest.startswith("✗") or "FAIL" in rest or "ERROR" in rest:
                label = repo or "repo"
                return f"  {DIM}{t}{RST}  {RED}✗{RST}  {RED}github {label}{RST}  {DIM}{rest}{RST}"
            if len(rest) > 80:
                return None
            return f"  {DIM}{t}{RST}  {DIM}▸  {rest}{RST}"
        if " FAIL" in body or " ERROR" in body or " TIMEOUT" in body:
            short = body.split("job:", 1)[-1]
            if len(short) > 60:
                short = short[:57] + "…"
            return f"  {DIM}{t}{RST}  {RED}✗{RST}  {RED}{short}{RST}"
        if body.endswith(" OK") or " RUN  " in body:
            return None
        return None
    if "ERR" in body or "DOWN" in body:
        return f"  {DIM}{t}{RST}  {RED}✗{RST}  {RED}{body}{RST}"
    if len(body) > 120:
        return None
    return f"  {DIM}{t}  {body}{RST}"


def follow() -> int:
    banner()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.touch(exist_ok=True)
    try:
        existing = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        existing = []
    buf: list[str] = []
    for raw in existing[-200:]:
        out = format_line(raw)
        if out:
            buf.append(out)
    for out in buf[-18:]:
        print(out, flush=True)

    with LOG.open("r", encoding="utf-8", errors="replace") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.25)
                continue
            out = format_line(line)
            if out:
                print(out, flush=True)


if __name__ == "__main__":
    _install_handlers()
    try:
        sys.exit(follow())
    except KeyboardInterrupt:
        stop_everything("Ctrl-C")
        sys.exit(0)
