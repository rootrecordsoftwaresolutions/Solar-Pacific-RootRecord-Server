#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
echo "=== voices ==="
grep -v '^#' "$ROOT/config/voices.conf" | grep -v '^[[:space:]]*$' || true
echo "=== relay ==="
grep -v '^#' "$ROOT/config/relay.conf" | grep -v '^[[:space:]]*$' || true
echo "=== processes ==="
pgrep -af 'council-relay|apps.council' || echo "(none)"
bash /home/rootrecord/.ollama/skills/plumbing/scripts/single-flight.sh status 2>/dev/null || true
# shellcheck disable=SC1091
source "$HERE/load_env.sh" /home/rootrecord/.config/ava-council/secrets.env /home/rootrecord/master/master-key.env 2>/dev/null || true
for k in TELEGRAM_AVA_TOKEN TELEGRAM_BRUCE_TOKEN TELEGRAM_CARLY_TOKEN AVA_TELEGRAM_BOT_TOKEN TELEGRAM_BOT_TOKEN; do
  if [[ -n "${!k:-}" ]]; then echo "[ok] $k=set"; else echo "[missing] $k"; fi
done
