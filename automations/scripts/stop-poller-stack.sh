#!/usr/bin/env bash
# ==============================================================================
# stop-poller-stack.sh — stop EVERY rootserver poller / cloudflared / unit process
# ------------------------------------------------------------------------------
# Used by: Ctrl-C / window close (poller-watch), rootserver-poller stop,
#          do-stack-reload.sh.
# Does NOT stop ava-ecoflow-ble (single BLE owner stays).
# Layout style (standing): keep SECTION banners.
# ==============================================================================
set -u

# ====================================================
# SECTION: CONFIG
# ====================================================
UNIT=rr-rootserver-poller.service

# ====================================================
# SECTION: STOP UNIT
# ====================================================
echo "[stop] stopping systemd unit ${UNIT}…"
systemctl --user stop "${UNIT}" 2>/dev/null || true

# ====================================================
# SECTION: MATCH KILLS (soft then hard)
# ====================================================
kill_match() {
  local pat="$1"
  local pids
  pids=$(pgrep -f "$pat" 2>/dev/null || true)
  if [ -n "$pids" ]; then
    echo "[stop] kill $pat -> $pids"
    # shellcheck disable=SC2086
    kill $pids 2>/dev/null || true
  fi
}

kill_match 'rootserver_poller\.py'
kill_match 'automations/bin/cloudflared'
kill_match 'automations/scripts/poller-watch\.py'
kill_match 'a-eyes/scripts/cam_server\.py'

sleep 1

for pat in 'rootserver_poller\.py' 'automations/bin/cloudflared' 'automations/scripts/poller-watch\.py' 'a-eyes/scripts/cam_server\.py'; do
  pids=$(pgrep -f "$pat" 2>/dev/null || true)
  if [ -n "$pids" ]; then
    echo "[stop] kill -9 $pat -> $pids"
    # shellcheck disable=SC2086
    kill -9 $pids 2>/dev/null || true
  fi
done

echo "[stop] stack down."
