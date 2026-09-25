#!/usr/bin/env bash
# ============================================================================
# energy/scripts/ble/ble-start.sh — start single BLE owner
# ----------------------------------------------------------------------------
# WHAT: Start ava-ecoflow-ble.service (user systemd). Do not dual-start owners.
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
UNIT=ava-ecoflow-ble.service
systemctl --user daemon-reload
systemctl --user start "$UNIT"
systemctl --user --no-pager --full status "$UNIT" | head -20
