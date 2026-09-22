#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

LOG="$ROOT/logs/ssh-relay.log"

echo "[$(date -u +%FT%TZ)] SSH relay started" | tee -a "$LOG"

if [[ -f "$ROOT/config/ssh-relay.env" ]]; then
    source "$ROOT/config/ssh-relay.env"
fi

while true; do
    if [[ -f "$ROOT/data/outbox.ndjson" ]]; then
        echo "[$(date -u +%FT%TZ)] Outbox detected" >> "$LOG"
    fi
    sleep "${RELAY_INTERVAL_SECONDS:-300}"
done
