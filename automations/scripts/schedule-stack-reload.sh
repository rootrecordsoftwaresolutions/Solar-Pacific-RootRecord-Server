#!/usr/bin/env bash
# ==============================================================================
# schedule-stack-reload.sh
#
# When GitHub pulls new skills code, fully stop every process the poller stack
# operates, then start clean so new edits load without a manual restart.
#
# Standing format for all future builds — invoke with: bash this-script.sh
# ==============================================================================
set -u

BAK_ROOT="${BAK_ROOT:-/home/rootrecord/Database/GITHUB}"
FLAG="$BAK_ROOT/flags/reload-poller-stack"
LOCK="/tmp/rootrecord-stack-reload.lock"
STAMP="$BAK_ROOT/flags/last-stack-reload"
LOG="/home/rootrecord/.ollama/skills/logs/store/stack-reload.log"
STOP="/home/rootrecord/.ollama/skills/automations/scripts/stop-poller-stack.sh"
CLI="/home/rootrecord/rootserver-poller"
UNIT="rr-rootserver-poller.service"

mkdir -p "$(dirname "$LOG")" "$BAK_ROOT/flags"

if [[ ! -f "$FLAG" ]]; then
  echo "[reload] no flag — nothing to do"
  exit 0
fi

if ! ( set -o noclobber; echo "$$" > "$LOCK" ) 2>/dev/null; then
  echo "[reload] already in progress — skip"
  exit 0
fi

if [[ -f "$STAMP" ]]; then
  last=$(cat "$STAMP" 2>/dev/null || echo 0)
  now=$(date +%s)
  if [[ "$last" =~ ^[0-9]+$ ]] && (( now - last < 60 )); then
    echo "[reload] debounced (last reload epoch=$last)"
    rm -f "$LOCK"
    exit 0
  fi
fi

echo "[reload] armed — full poller stack stop/start in 8s"
echo "[reload] flag=$(tr '\n' ' ' < "$FLAG" 2>/dev/null || true)"
echo "[reload] log=$LOG"

# Deferred so github_sync_all can exit; always bash stop script (may not be +x).
nohup bash -c "
  set +e
  exec >>'$LOG' 2>&1
  echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) stack-reload BEGIN\"
  sleep 8
  if [[ -f '$STOP' ]]; then
    bash '$STOP'
  else
    systemctl --user stop '$UNIT' 2>/dev/null || true
    pkill -f 'rootserver_poller\\.py' 2>/dev/null || true
    pkill -f 'automations/bin/cloudflared' 2>/dev/null || true
    pkill -f 'poller-watch\\.py' 2>/dev/null || true
  fi
  rm -f /tmp/ecoflow-ble.lock 2>/dev/null || true
  systemctl --user daemon-reload 2>/dev/null || true
  sleep 1
  if systemctl --user start '$UNIT' 2>/dev/null; then
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) started $UNIT\"
  elif [[ -f '$CLI' || -x '$CLI' ]]; then
    bash '$CLI' start 2>/dev/null || '$CLI' start 2>/dev/null || true
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) started via $CLI\"
  else
    echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) FAIL: no unit and no CLI\"
  fi
  date +%s > '$STAMP'
  rm -f '$FLAG'
  rm -f '$LOCK'
  echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) stack-reload END\"
" >/dev/null 2>&1 &

disown 2>/dev/null || true
echo "[reload] scheduled (log=$LOG)"
exit 0
