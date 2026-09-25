#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-energy-backup-off.sh - Delta2 energy backup OFF
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on delta2: method=enable_energy_backup want=off.
# HOW:  ROOT/lib/py -> action_runner.py (eflib + bleak). Use flock when scheduled.
# RULE: Never invent watts/SOC. BLE down -> non-zero / WAITING.
# Layout style (standing): keep this header so the file is self-explanatory.
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "delta2" --method "enable_energy_backup" --want "off" --label "Delta2 energy backup OFF"
