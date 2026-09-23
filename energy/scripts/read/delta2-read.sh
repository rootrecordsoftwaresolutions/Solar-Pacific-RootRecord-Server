#!/usr/bin/env bash
# Live read delta2 — WAITING/No data if BLE unavailable; never invent watts.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/read_runner.py" --device "delta2"
