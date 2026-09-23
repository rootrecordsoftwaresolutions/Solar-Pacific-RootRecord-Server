#!/usr/bin/env python3
"""Minimal INI reader for devices.conf (stdlib only)."""
from __future__ import annotations
import configparser
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from paths import CONFIG  # noqa: E402

def load(path: Path | None = None) -> configparser.ConfigParser:
    cp = configparser.ConfigParser()
    cp.read(path or CONFIG)
    return cp

def device(alias: str) -> dict:
    cp = load()
    if alias not in cp:
        raise KeyError(f"unknown device alias: {alias}")
    return dict(cp[alias])
