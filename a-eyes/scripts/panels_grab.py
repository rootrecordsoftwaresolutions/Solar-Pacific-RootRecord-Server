#!/usr/bin/env python3
"""Grab one JPEG from Night Owl RTSP using store/CONNECTION.json."""
from __future__ import annotations
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
STORE = SKILL / "store"
DB_FRAMES = Path("/home/rootrecord/Database/A-EYES/frames")
FRAMES = DB_FRAMES
CONN_PATH = STORE / "CONNECTION.json"


def load_conn() -> dict:
    if not CONN_PATH.is_file():
        raise FileNotFoundError(f"missing {CONN_PATH}")
    return json.loads(CONN_PATH.read_text(encoding="utf-8"))


def rtsp_url(channel: int = 1, stream: int = 0) -> str:
    conn = load_conn()
    lan = conn.get("lan") or {}
    urls = lan.get("rtsp_urls") or {}
    key = "channel_main" if int(stream) == 0 else "channel_sub"
    tmpl = urls.get(key) or urls.get("channel_main")
    if not tmpl:
        ip = lan.get("ip") or "192.168.1.33"
        user = lan.get("rtsp_user") or "admin"
        pw = lan.get("rtsp_password") or "admin"
        return f"rtsp://{user}:{pw}@{ip}:554/user={user}&password={pw}&channel={channel}&stream={stream}"
    return tmpl.replace("{N}", str(channel))


def grab_jpeg(channel: int = 1, stream: int = 0, out: Path | None = None) -> Path:
    DB_FRAMES.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out or (FRAMES / f"ch{channel}-{ts}.jpg")
    url = rtsp_url(channel, stream)
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-rtsp_transport", "tcp",
        "-i", url,
        "-frames:v", "1",
        "-q:v", "2",
        str(path),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0 or not path.is_file() or path.stat().st_size < 100:
        err = (r.stderr or r.stdout or "ffmpeg failed").strip()[:300]
        raise RuntimeError(err or "empty jpeg")
    return path


if __name__ == "__main__":
    ch = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    p = grab_jpeg(channel=ch)
    print(f"OK {p}")
