#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-grid-bypass-on.sh - Delta2 grid bypass ON
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=disable_grid_bypass want=on.
# HOW:  ROOT/lib/py -> action_runner.py. Confirm on/off meaning before scheduling.
# RULE: Never invent watts/SOC. BLE down -> non-zero / WAITING.
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "delta2" --method "disable_grid_bypass" --want "on" --label "Delta2 grid bypass ON"
