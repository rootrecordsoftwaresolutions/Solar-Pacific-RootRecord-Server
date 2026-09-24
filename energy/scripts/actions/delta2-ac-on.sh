#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-ac-on.sh - Delta2 AC ON
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=enable_ac_ports want=on.
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
  --method "enable_ac_ports" \
  --want "on" \
  --label "Delta2 AC ON"
