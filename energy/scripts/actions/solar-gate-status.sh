#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/solar-gate-status.sh - solar USB gate policy (status)
# -----------------------------------------------------------------------------
# WHAT: Print solar-gate-state.json or WAITING if missing.
# =============================================================================
set -euo pipefail
STATE="/home/rootrecord/Database/ENERGY/ports/solar-gate-state.json"
if [[ -f "$STATE" ]]; then cat "$STATE"; else echo "WAITING"; echo "No data - solar gate state not written yet"; exit 2; fi
