#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting RootRecord SSH Globe Relay"

if [[ -f "/home/rootrecord/master/master-key.env" ]]; then
    source "/home/rootrecord/master/master-key.env"
else
    echo "ERROR: /home/rootrecord/master/master-key.env not found"
    exit 1
fi

mkdir -p "$ROOT/logs" "$ROOT/data"

if [[ -x "$ROOT/scripts/health-check.sh" ]]; then
    "$ROOT/scripts/health-check.sh"
fi

echo "Launching relay..."
"$ROOT/scripts/ssh-relay.sh"
