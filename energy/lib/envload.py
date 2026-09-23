#!/usr/bin/env python3
"""Load EcoFlow keys from central master-key.env only. Never print secrets."""
from __future__ import annotations
import os
from pathlib import Path

# Single secrets root — no Ava-Core path.
MASTER_KEY_ENV = Path("/home/rootrecord/master/master-key.env")

# Least privilege: only keys energy BLE needs (plus SN aliases).
ALLOW = frozenset({
    "AVA_ECOFLOW_USER_ID",
    "ECOFLOW_ACCOUNT_ID",
    "ECOFLOW_DELTA_2",
    "ECOFLOW_RIVER_2_PRO",
    "ECOFLOW_DELTA_2_SECONDARY",
})


def load_env(paths: list[Path] | None = None) -> None:
    for env in paths or [MASTER_KEY_ENV]:
        if not env.is_file():
            continue
        for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, _, v = s.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if not k or k not in ALLOW:
                continue
            if k not in os.environ:
                os.environ[k] = v


def user_id() -> str:
    """BLE connect user id — AVA_ECOFLOW_USER_ID, else ECOFLOW_ACCOUNT_ID."""
    load_env()
    uid = (os.environ.get("AVA_ECOFLOW_USER_ID") or "").strip()
    if not uid:
        uid = (os.environ.get("ECOFLOW_ACCOUNT_ID") or "").strip()
    return uid
