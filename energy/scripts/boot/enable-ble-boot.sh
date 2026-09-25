#!/usr/bin/env bash
# ============================================================================
# energy/scripts/boot/enable-ble-boot.sh — enable BLE owner at login
# ----------------------------------------------------------------------------
# WHAT: systemctl --user enable --now ava-ecoflow-ble.service
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
UNIT=ava-ecoflow-ble.service
systemctl --user daemon-reload
systemctl --user enable --now "$UNIT"
systemctl --user is-enabled "$UNIT"
systemctl --user is-active "$UNIT"
