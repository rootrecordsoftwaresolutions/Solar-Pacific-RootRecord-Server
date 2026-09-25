#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-ac-charging-on.sh - Delta2 AC charging ON
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=enable_ac_charging want=on.
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
  --want "on" \
  --label "Delta2 AC charging ON"
