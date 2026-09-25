#!/usr/bin/env bash
# ============================================================================
# energy/scripts/ble/ble-status.sh — BLE owner unit + log peek
# ----------------------------------------------------------------------------
# WHAT: systemctl status + tail of ava-ecoflow-ble.log
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
UNIT=ava-ecoflow-ble.service
LOG="${HOME}/.ollama/skills/logs/store/ava-ecoflow-ble.log"
echo "=== systemctl --user status $UNIT ==="
systemctl --user --no-pager --full status "$UNIT" 2>/dev/null | head -25 || echo "(unit not found)"
echo "=== tail log $LOG ==="
tail -20 "$LOG" 2>/dev/null || echo "(no log yet)"
