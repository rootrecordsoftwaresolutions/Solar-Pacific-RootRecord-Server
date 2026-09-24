#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/solar-gate-arm.sh - solar USB gate policy (arm)
# -----------------------------------------------------------------------------
# WHAT: Local policy file only (no live PV watts invented).
# HOW:  Writes Database/ENERGY/ports/solar-gate-state.json
# =============================================================================
set -euo pipefail
STATE="/home/rootrecord/Database/ENERGY/ports/solar-gate-state.json"
mkdir -p "$(dirname "$STATE")"
printf '%s\n' "{\"enabled\": true, \"pv_gate_w\": 400, \"note\": \"policy armed; USB toggles via delta2-usb-*; no live PV invented\", \"at\": \"$(date -Iseconds)\"}" > "$STATE"
echo "STATUS=OK policy armed (no watts invented)"
