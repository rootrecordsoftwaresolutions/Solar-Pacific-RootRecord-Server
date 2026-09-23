#!/usr/bin/env bash
# ==============================================================================
# # INFO — telegram council status (no secret values)
# ------------------------------------------------------------------------------
# Process match: ^python3 …council-relay.py only (no bash/pgrep false positives).
# Bak: /home/rootrecord/Database/GITHUB/
# ==============================================================================
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
echo "=== relay.conf ==="
grep -v '^#' "$ROOT/config/relay.conf" | grep -v '^[[:space:]]*$' || true
echo "=== processes (^python3 argv only) ==="
if pgrep -af '^python3 .+/council-relay\.py' >/dev/null 2>&1; then
  pgrep -af '^python3 .+/council-relay\.py'
else
  echo "(no council-relay.py)"
fi
if pgrep -af '^python3 .+apps\.council' >/dev/null 2>&1; then
  pgrep -af '^python3 .+apps\.council'
else
  echo "(no apps.council)"
fi
echo "=== secrets present? (names only) ==="
# shellcheck disable=SC1091
source "$HERE/load_env.sh" /home/rootrecord/.config/ava-council/secrets.env /home/rootrecord/master/master-key.env 2>/dev/null || true
for k in AVA_TELEGRAM_BOT_TOKEN TELEGRAM_BRUCE_TOKEN TELEGRAM_CARLY_TOKEN TELEGRAM_BOT_TOKEN; do
  if [[ -n "${!k:-}" ]]; then echo "$k=set"; else echo "$k=missing"; fi
done
