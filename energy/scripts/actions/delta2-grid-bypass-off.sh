#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-grid-bypass-off.sh - Delta2 grid bypass OFF
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=disable_grid_bypass want=off.
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "delta2" --method "disable_grid_bypass" --want "off" --label "Delta2 grid bypass OFF"
