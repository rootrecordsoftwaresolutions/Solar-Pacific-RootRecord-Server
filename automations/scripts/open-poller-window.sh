#!/usr/bin/env bash
# Open a titled terminal that shows live poller + cloudflared lines.
# Does NOT start a second poller — systemd owns the process.
set -euo pipefail
LOG="${HOME}/.ollama/skills/logs/store/rootserver-poller.log"
TITLE="RootRecord poller — rootserver"
mkdir -p "$(dirname "$LOG")"
touch "$LOG"

# Prefer gnome-terminal; fall back to x-terminal-emulator.
if command -v gnome-terminal >/dev/null 2>&1; then
  exec gnome-terminal --title="$TITLE" --geometry=120x32 -- bash -lc "
    echo '=== RootRecord poller window ==='
    echo \"Log: $LOG\"
    systemctl --user is-active rr-rootserver-poller.service 2>/dev/null || true
    echo '--- live (Ctrl-C closes window only; service keeps running) ---'
    exec tail -n 40 -F '$LOG'
  "
fi
exec x-terminal-emulator -T "$TITLE" -e bash -lc "tail -n 40 -F '$LOG'"
