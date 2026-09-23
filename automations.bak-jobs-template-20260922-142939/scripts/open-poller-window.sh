#!/usr/bin/env bash
# Open a titled terminal with a colored live poller view.
# Does NOT start a second poller — systemd owns the process.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WATCH="$ROOT/scripts/poller-watch.py"
TITLE="RootRecord poller — rootserver"
export POLLER_LOG="${POLLER_LOG:-$HOME/.ollama/skills/logs/store/rootserver-poller.log}"
mkdir -p "$(dirname "$POLLER_LOG")"
touch "$POLLER_LOG"

if command -v gnome-terminal >/dev/null 2>&1; then
  exec gnome-terminal --title="$TITLE" --geometry=100x36 -- \
    bash -lc "exec /usr/bin/python3 '$WATCH'"
fi
exec x-terminal-emulator -T "$TITLE" -e /usr/bin/python3 "$WATCH"
