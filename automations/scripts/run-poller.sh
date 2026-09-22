#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MASTER_ENV="${MASTER_ENV:-/home/rootrecord/master/master-key.env}"
if [[ -f "$MASTER_ENV" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$MASTER_ENV"
  set +a
fi
export POLLER_BIND="${POLLER_BIND:-127.0.0.1}"
export POLLER_PORT="${POLLER_PORT:-8799}"
export POLLER_INTERVAL_SEC="${POLLER_INTERVAL_SEC:-5}"
export POLLER_PUBLIC_HOST="${POLLER_PUBLIC_HOST:-rootserver.rootrecord.cloud}"
export POLLER_ENABLE_TUNNEL="${POLLER_ENABLE_TUNNEL:-1}"
export POLLER_TUNNEL_MODE="${POLLER_TUNNEL_MODE:-token}"
export CLOUDFLARED_BIN="${CLOUDFLARED_BIN:-$ROOT/bin/cloudflared}"
export CLOUDFLARED_TOKEN_FILE="${CLOUDFLARED_TOKEN_FILE:-${AVA_TUNNEL_TOKEN_FILE:-$HOME/.cloudflared/origin.token}}"
exec /usr/bin/python3 "$ROOT/scripts/rootserver_poller.py"
