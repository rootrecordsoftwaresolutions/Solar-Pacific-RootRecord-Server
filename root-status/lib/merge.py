"""Merge energy + system clean status JSONs into one central 5min transmission file."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import paths

def _load(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def merge() -> Path:
    paths.ensure_dirs()
    energy = _load(paths.ENERGY_STATUS)
    system = _load(paths.SYSTEM_STATUS)
    payload = {
        "skill": "root-status",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "energy": energy or None,
        "system": system or None,
    }
    tmp = paths.MERGED.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    tmp.replace(paths.MERGED)
    return paths.MERGED
