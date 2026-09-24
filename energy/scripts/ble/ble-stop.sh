#!/usr/bin/env bash
# ============================================================================
# energy/scripts/ble/ble-stop.sh — stop single BLE owner
# ----------------------------------------------------------------------------
# WHAT: Stop ava-ecoflow-ble.service only (does not stop the rootserver poller).
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
UNIT=ava-ecoflow-ble.service
systemctl --user stop "$UNIT" || true
systemctl --user --no-pager --full status "$UNIT" 2>/dev/null | head -15 || true
