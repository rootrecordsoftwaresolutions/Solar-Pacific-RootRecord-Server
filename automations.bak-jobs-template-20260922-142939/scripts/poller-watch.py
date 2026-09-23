#!/usr/bin/env python3
"""Pretty live view of the rootserver poller log (colors + filter)."""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

LOG = Path(
    os.environ.get(
        "POLLER_LOG",
        str(Path.home() / ".ollama/skills/logs/store/rootserver-poller.log"),
    )
)
HOST = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
LOCAL = os.environ.get("POLLER_LOCAL", "http://127.0.0.1:8799/")

# ANSI
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
BG = "\033[40m"


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
    print(f"{CYAN}│{RST}  log      {DIM}{LOG}{RST}", flush=True)
    print(f"{CYAN}│{RST}  {DIM}Ctrl-C closes this window only — service keeps running{RST}", flush=True)
    print(f"{CYAN}{BOLD}╰{bar}──{RST}", flush=True)
    print(flush=True)


def split_ts(line: str) -> tuple[str, str]:
    # 2026-09-22T14:18:19-10:00rest
    if len(line) >= 25 and line[4] == "-" and "T" in line[:20]:
        # find end of offset +HH:MM or -HH:MM
        for i, ch in enumerate(line):
            if i > 19 and ch in ("P", "T", "c", "H", "W") and i > 20:
                # weak — prefer ISO end at +HH:MM / -HH:MM after seconds
                pass
        # timestamps are like 2026-09-22T14:18:19-10:00
        if len(line) >= 25 and line[19] in "+-" and line[22] == ":":
            return line[:25], line[25:]
        if len(line) >= 30 and line[26] in "+-" :  # with ms unlikely
            return line[:32], line[32:]
    # try: first 25 chars if looks iso
    if len(line) > 25 and line[10] == "T":
        return line[:25], line[25:]
    return "", line


def clock(ts: str) -> str:
    # show HH:MM:SS from ISO
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

    # Drop residual noise if old log still has it
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

    # Old verbose cloudflared: lines
    if body.startswith("cloudflared: "):
        raw_cf = body[len("cloudflared: "):]
        if "Registered tunnel connection" in raw_cf:
            bits = _edge_bits(raw_cf)
            return f"  {DIM}{t}{RST}  {CYAN}◆{RST}  {CYAN}tunnel connected{RST}  {DIM}{bits}{RST}"
        if "Starting tunnel" in raw_cf:
            return f"  {DIM}{t}{RST}  {MAGENTA}▲{RST}  {MAGENTA}tunnel starting{RST}"
        if " ERR " in f" {raw_cf} " or raw_cf.startswith("ERR ") or " error=" in raw_cf.lower():
            short = "tunnel error"
            if "timeout" in raw_cf.lower():
                short = "tunnel timeout — reconnecting"
            elif "terminated" in raw_cf.lower():
                short = "tunnel connection terminated"
            return f"  {DIM}{t}{RST}  {YELLOW}!{RST}  {YELLOW}{short}{RST}"
        if " WRN " in f" {raw_cf} " or raw_cf.startswith("WRN "):
            short = "tunnel warn"
            if "timeout" in raw_cf.lower():
                short = "tunnel timeout — reconnecting"
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
    if body.startswith("cloudflared ERR") or "DOWN" in body:
        return f"  {DIM}{t}{RST}  {RED}✗{RST}  {RED}{body}{RST}"
    # default: keep short dim crumbs only
    if len(body) > 120:
        return None
    return f"  {DIM}{t}  {body}{RST}"


def follow() -> int:
    banner()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.touch(exist_ok=True)
    # Show last ~30 interesting lines, then follow
    try:
        existing = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        existing = []
    # Collect interesting lines, then print only the last 18 (clean desk view).
    buf: list[str] = []
    for raw in existing[-200:]:
        out = format_line(raw)
        if out:
            buf.append(out)
    for out in buf[-18:]:
        print(out, flush=True)
    # follow with tail -F via reading file grow (portable)
    with LOG.open("r", encoding="utf-8", errors="replace") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            out = format_line(line)
            if out:
                print(out, flush=True)


if __name__ == "__main__":
    try:
        sys.exit(follow())
    except KeyboardInterrupt:
        print(f"\n{DIM}window closed — service still running{RST}")
        sys.exit(0)
