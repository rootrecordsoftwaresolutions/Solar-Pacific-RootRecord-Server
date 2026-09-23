#!/usr/bin/env bash
# Live read river2pro — WAITING/No data if BLE unavailable; never invent watts.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/read_runner.py" --device "river2pro"
