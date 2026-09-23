#!/usr/bin/env bash
# INFO — MUST HAVE: stop EVERY rootserver poller / cloudflared / unit process.
set -u
UNIT=rr-rootserver-poller.service
echo "[stop] stopping systemd unit ${UNIT}…"
systemctl --user stop "${UNIT}" 2>/dev/null || true

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

sleep 1

# hard kill leftovers
for pat in 'rootserver_poller\.py' 'automations/bin/cloudflared' 'automations/scripts/poller-watch\.py'; do
  pids=$(pgrep -f "$pat" 2>/dev/null || true)
  if [ -n "$pids" ]; then
    echo "[stop] kill -9 $pat -> $pids"
    # shellcheck disable=SC2086
    kill -9 $pids 2>/dev/null || true
  fi
done

echo "[stop] stack down."
