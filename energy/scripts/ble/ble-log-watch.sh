#!/usr/bin/env bash
# ============================================================================
# energy/scripts/ble/ble-log-watch.sh — follow BLE log (foreground)
# ----------------------------------------------------------------------------
# WHAT: tail -F ava-ecoflow-ble.log. Ctrl-C stops watch only (not the unit).
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
LOG="${HOME}/.ollama/skills/logs/store/ava-ecoflow-ble.log"
mkdir -p "$(dirname "$LOG")"
touch "$LOG"
exec tail -F "$LOG"
