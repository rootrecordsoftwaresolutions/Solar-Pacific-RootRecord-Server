#!/usr/bin/env bash
# ============================================================================
# energy/scripts/read/delta2-read.sh — live EcoFlow BLE read (Delta 2 / B2)
# ----------------------------------------------------------------------------
# WHAT: Snapshot Delta 2 → SQLite (canonical) + legacy JSON last-files.
# HOW:  ROOT/lib/py → lib/read_runner.py --device delta2
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
exec "$ROOT/lib/py" "$ROOT/lib/read_runner.py" --device "delta2"
