#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-ac-charging-off.sh - Delta2 AC charging OFF
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=enable_ac_charging want=off.
# HOW:  ROOT/lib/py -> action_runner.py (eflib + bleak). Use flock when scheduled.
# RULE: Never invent watts/SOC. BLE down -> non-zero / WAITING.
# Layout style (standing): keep this header so the file is self-explanatory.
# =============================================================================
set -euo pipefail

# ====================================================
# SECTION: PATHS
# ====================================================
ROOT="/home/rootrecord/.ollama/skills/energy"

# ====================================================
# SECTION: RUN
# ====================================================
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_ac_charging" \
  --want "off" \
  --label "Delta2 AC charging OFF"
