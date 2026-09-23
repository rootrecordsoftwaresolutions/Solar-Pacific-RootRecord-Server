#!/usr/bin/env bash
# Solar USB gate policy stub — atomic ports first; no fake PV watts.
set -euo pipefail
STATE="/home/rootrecord/Database/ENERGY/ports/solar-gate-state.json"
MODE="arm"
mkdir -p "$(dirname "$STATE")"
case "$MODE" in
  status)
    if [[ -f "$STATE" ]]; then cat "$STATE"; else echo "WAITING"; echo "No data — solar gate state not written yet"; exit 2; fi
    ;;
  arm)
    printf '%s\n' '{"enabled": true, "pv_gate_w": 400, "note": "policy armed; USB toggles via delta2-usb-*; no live PV invented", "at": "'"$(date -Iseconds)"'"}' > "$STATE"
    echo "STATUS=OK policy armed (no watts invented)"
    ;;
  disarm)
    printf '%s\n' '{"enabled": false, "note": "policy disarmed", "at": "'"$(date -Iseconds)"'"}' > "$STATE"
    echo "STATUS=OK policy disarmed"
    ;;
esac
