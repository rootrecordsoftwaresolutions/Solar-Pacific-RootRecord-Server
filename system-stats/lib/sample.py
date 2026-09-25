#!/usr/bin/env python3
"""One system snapshot: CPU%, load, mem. Same state semantics as energy."""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from paths import CPU, LAST, LOAD, MEM, SAMPLES, ensure_dirs

LOCAL = ZoneInfo("Pacific/Honolulu")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _local_stamp() -> str:
    return datetime.now(LOCAL).strftime("%Y%m%d-%H%M%S")


def _read_load():
    try:
        with open("/proc/loadavg", encoding="utf-8") as f:
            a, b, c, *_ = f.read().split()
        return float(a), float(b), float(c), "measured"
    except OSError:
        return None, None, None, "missing"


def _read_mem():
    total = avail = None
    try:
        with open("/proc/meminfo", encoding="utf-8") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    total = int(line.split()[1]) * 1024
                elif line.startswith("MemAvailable:"):
                    avail = int(line.split()[1]) * 1024
        if total and avail is not None:
            used_pct = 100.0 * (1.0 - (avail / total))
            return total, avail, used_pct, "measured"
    except (OSError, ValueError, ZeroDivisionError):
        pass
    return None, None, None, "missing"


def _read_cpu_pct(sample_s: float = 0.35) -> tuple[float | None, str]:
    """Two-sample /proc/stat idle ratio → busy %."""
    def ticks():
        with open("/proc/stat", encoding="utf-8") as f:
            parts = f.readline().split()
        # cpu user nice system idle iowait irq softirq steal ...
        nums = [int(x) for x in parts[1:]]
        idle = nums[3] + (nums[4] if len(nums) > 4 else 0)
        total = sum(nums)
        return idle, total

    try:
        i1, t1 = ticks()
        time.sleep(sample_s)
        i2, t2 = ticks()
        dt, di = t2 - t1, i2 - i1
        if dt <= 0:
            return None, "missing"
        busy = 100.0 * (1.0 - (di / dt))
        return max(0.0, min(100.0, busy)), "measured"
    except (OSError, ValueError, ZeroDivisionError):
        return None, "missing"


def snapshot() -> dict:
    ensure_dirs()
    load1, load5, load15, load_st = _read_load()
    mem_total, mem_avail, mem_pct, mem_st = _read_mem()
    cpu_pct, cpu_st = _read_cpu_pct()
    at = _now_iso()
    fields = {
        "cpu_percent": {"value": round(cpu_pct, 2) if cpu_pct is not None else None, "state": cpu_st, "unit": "%"},
        "load1": {"value": load1, "state": load_st, "unit": "load"},
        "load5": {"value": load5, "state": load_st, "unit": "load"},
        "load15": {"value": load15, "state": load_st, "unit": "load"},
        "mem_total_bytes": {"value": mem_total, "state": mem_st, "unit": "B"},
        "mem_available_bytes": {"value": mem_avail, "state": mem_st, "unit": "B"},
        "mem_used_percent": {"value": round(mem_pct, 2) if mem_pct is not None else None, "state": mem_st, "unit": "%"},
    }
    return {
        "alias": "host",
        "host": os.uname().nodename,
        "fields": fields,
        "at": at,
        "source": "proc",
    }


def _atomic_write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def persist(snap: dict) -> Path:
    ensure_dirs()
    stamp = _local_stamp()
    sample_path = SAMPLES / f"sys-{stamp}.json"
    _atomic_write(sample_path, snap)

    f = snap["fields"]
    _atomic_write(LAST / "host-last.json", snap)
    _atomic_write(CPU / "host-last.json", {
        "cpu_percent": f["cpu_percent"]["value"],
        "state": f["cpu_percent"]["state"],
        "at": snap["at"],
    })
    _atomic_write(LOAD / "host-last.json", {
        "load1": f["load1"]["value"],
        "load5": f["load5"]["value"],
        "load15": f["load15"]["value"],
        "state": f["load1"]["state"],
        "at": snap["at"],
    })
    _atomic_write(MEM / "host-last.json", {
        "mem_used_percent": f["mem_used_percent"]["value"],
        "mem_available_bytes": f["mem_available_bytes"]["value"],
        "mem_total_bytes": f["mem_total_bytes"]["value"],
        "state": f["mem_used_percent"]["state"],
        "at": snap["at"],
    })
    return sample_path


def summary_line(snap: dict) -> str:
    f = snap["fields"]
    def v(key, fmt):
        cell = f.get(key) or {}
        if cell.get("state") != "measured" or cell.get("value") is None:
            return "—"
        return fmt(cell["value"])
    return (
        f"SYSTEM  cpu={v('cpu_percent', lambda x: f'{x:.0f}%')}  "
        f"load={v('load1', lambda x: f'{x:.2f}')}  "
        f"mem={v('mem_used_percent', lambda x: f'{x:.0f}%')}  "
        f"src=proc"
    )


def main() -> int:
    snap = snapshot()
    path = persist(snap)
    line = summary_line(snap)
    print(line)
    print(f"OK wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
