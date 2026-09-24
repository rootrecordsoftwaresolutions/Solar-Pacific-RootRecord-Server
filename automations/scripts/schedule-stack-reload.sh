#!/usr/bin/env bash
# ==============================================================================
# schedule-stack-reload.sh
#
# When GitHub pulls new skills code, fully stop every process the poller stack
# operates, then start clean so new edits load without a manual restart.
#
# Operated by this reload (closed, then restarted):
#   - rr-rootserver-poller.service
#   - rootserver_poller.py
#   - cloudflared (automations tunnel)
#   - poller-watch.py
#
# NOT stopped (separate ownership; must stay single-owner):
#   - ava-ecoflow-ble.service / ble-owner.py
#
# Design:
#   - Deferred (sleep) so github_sync_all can finish and release the job thread
#   - Single-flight lock — no parallel reloads
#   - Debounce — ignore if last reload was < 60s ago
#   - Never invent a second poller; only stop → start the existing unit/CLI
# ==============================================================================
set -u

BAK_ROOT="${BAK_ROOT:-/home/rootrecord/Database/GITHUB}"
FLAG="$BAK_ROOT/flags/reload-poller-stack"
LOCK="/tmp/rootrecord-stack-reload.lock"
STAMP="$BAK_ROOT/flags/last-stack-reload"
LOG="${POLLER_LOG:-/home/rootrecord/.ollama/skills/logs/store/stack-reload.log}"
STOP="/home/rootrecord/.ollama/skills/automations/scripts/stop-poller-stack.sh"
CLI="/home/rootrecord/rootserver-poller"
UNIT="rr-rootserver-poller.service"

mkdir -p "$(dirname "$LOG")" "$BAK_ROOT/flags"

if [[ ! -f "$FLAG" ]]; then
  exit 0
fi

# Single-flight: if a reload is already scheduled/running, do nothing.
if ! ( set -o noclobber; echo "$$" > "$LOCK" ) 2>/dev/null; then
  echo "[reload] already in progress — skip"
  exit 0
fi

# Debounce rapid successive pulls
if [[ -f "$STAMP" ]]; then
  last=$(cat "$STAMP" 2>/dev/null || echo 0)
  now=$(date +%s)
  if [[ "$last" =~ ^[0-9]+$ ]] && (( now - last < 60 )); then
    echo "[reload] debounced (last reload ${last}s epoch)"
    rm -f "$LOCK"
    exit 0
  fi
fi

echo "[reload] armed — full poller stack stop/start in 8s (flag=$(cat "$FLAG" 2>/dev/null | tr '\n' ' '))"

nohup bash -c "
  set +e
  exec >>'$LOG' 2>&1
  echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) stack-reload BEGIN\"
  sleep 8
  if [[ -x '$STOP' ]]; then
    bash '$STOP'
  else
    systemctl --user stop '$UNIT' 2>/dev/null || true
    pkill -f 'rootserver_poller\\.py' 2>/dev/null || true
    pkill -f 'automations/bin/cloudflared' 2>/dev/null || true
    pkill -f 'poller-watch\\.py' 2>/dev/null || true
  fi
  # Drop stale BLE action flock if holder died with the poller job thread
  rm -f /tmp/ecoflow-ble.lock 2>/dev/null || true
  systemctl --user daemon-reload 2>/dev/null || true
  sleep 1
  if systemctl --user start '$UNIT' 2>/dev/null; then
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) started $UNIT\"
  elif [[ -x '$CLI' ]]; then
    '$CLI' start
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) started via $CLI\"
  else
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) FAIL: no unit and no CLI\"
  fi
  date +%s > '$STAMP'
  rm -f '$FLAG'
  rm -f '$LOCK'
  echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) stack-reload END\"
" >/dev/null 2>&1 &

disown || true
echo "[reload] scheduled (log=$LOG)"
exit 0
