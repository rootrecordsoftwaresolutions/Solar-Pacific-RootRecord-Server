#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/solar-gate-disarm.sh - solar USB gate policy (disarm)
# -----------------------------------------------------------------------------
# WHAT: Local policy file only (no live PV watts invented).
# =============================================================================
set -euo pipefail
STATE="/home/rootrecord/Database/ENERGY/ports/solar-gate-state.json"
mkdir -p "$(dirname "$STATE")"
printf '%s\n' "{\"enabled\": false, \"note\": \"policy disarmed\", \"at\": \"$(date -Iseconds)\"}" > "$STATE"
echo "STATUS=OK policy disarmed"
