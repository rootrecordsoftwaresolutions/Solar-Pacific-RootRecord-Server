#!/usr/bin/env bash
# Manual foreground poller. Start it, leave it running, Ctrl+C to stop.
set -uo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCK_FILE="/tmp/github-skill-poller.lock"
POLL_INTERVAL_SECONDS=300

if command -v flock >/dev/null 2>&1; then
  exec 9>"$LOCK_FILE"
  flock -n 9 || { echo "github-skill poller already running."; exit 1; }
fi

echo "github-skill poller starting. Polling every ${POLL_INTERVAL_SECONDS}s."
echo "Log: $SELF_DIR/poll-and-push.log"
echo "Ctrl+C to stop."
echo

trap 'echo; echo "Stopped."; exit 0' INT TERM

while true; do
  bash "$SELF_DIR/push-once.sh"
  sleep "$POLL_INTERVAL_SECONDS"
done
