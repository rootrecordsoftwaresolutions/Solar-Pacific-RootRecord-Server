#!/usr/bin/env python3
"""Grab one JPEG still from a camera channel and save it to the Database.

This script does exactly one thing: pull a single frame via RTSP/ffmpeg
and write it to /home/rootrecord/Database/A-EYES/frames/. Nothing else
reads it, mirrors it, or serves it — that's the gateway's job.
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
CONN_PATH = SKILL / "store" / "CONNECTION.json"
MASTER_KEY = Path("/home/rootrecord/master/master-key.env")
DB_FRAMES = Path("/home/rootrecord/Database/A-EYES/frames")


def load_master_key(name: str) -> str:
    if not MASTER_KEY.is_file():
        raise FileNotFoundError(f"missing {MASTER_KEY}")
    for line in MASTER_KEY.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k.strip() == name:
            return v.strip().strip('"').strip("'")
    raise KeyError(f"{name} not found in {MASTER_KEY}")


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
    user = lan.get("rtsp_user") or "admin"
    pw = load_master_key("AEYES_RTSP_PASSWORD")
    if not tmpl:
        ip = lan.get("ip") or "192.168.1.33"
        return f"rtsp://{user}:{pw}@{ip}:554/user={user}&password={pw}&channel={channel}&stream={stream}"
    return tmpl.replace("{USER}", user).replace("{PASS}", pw).replace("{N}", str(channel))


def grab_jpeg(channel: int = 1, stream: int = 0) -> Path:
    DB_FRAMES.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = DB_FRAMES / f"ch{channel}-{ts}.jpg"
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
