#!/usr/bin/env bash
# ============================================================================
# energy/scripts/read/river2pro-read.sh — live EcoFlow BLE read (River 2 Pro / B1)
# ----------------------------------------------------------------------------
# WHAT: Snapshot River 2 Pro → SQLite (canonical) + legacy JSON last-files.
# HOW:  ROOT/lib/py → lib/read_runner.py --device river2pro
# RULE: Never invent watts/SOC. BLE down → non-zero / WAITING.
# Layout style (standing): keep this header so the file is self-explanatory.
# ============================================================================
set -euo pipefail

# ====================================================
# SECTION: PATHS
# ====================================================
ROOT="/home/rootrecord/.ollama/skills/energy"

# ====================================================
# SECTION: RUN
# ====================================================
exec "$ROOT/lib/py" "$ROOT/lib/read_runner.py" --device "river2pro"
