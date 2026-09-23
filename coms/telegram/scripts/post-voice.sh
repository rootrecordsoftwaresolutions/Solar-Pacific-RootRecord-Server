#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VOICE="${1:?voice}"; shift
TEXT="${*:?text}"
# shellcheck disable=SC1091
source "$HERE/load_env.sh" \
  /home/rootrecord/.config/ava-council/secrets.env \
  /home/rootrecord/master/master-key.env
TOKEN_ENV=$(awk -F'\t' -v v="$VOICE" '$1==v && $2=="1" {print $4; exit}' "$ROOT/config/voices.conf")
[[ -n "$TOKEN_ENV" ]] || { echo "unknown/disabled voice: $VOICE" >&2; exit 2; }
TOKEN="${!TOKEN_ENV:-}"
if [[ -z "$TOKEN" && "$VOICE" == "ava" ]]; then
  TOKEN="${AVA_TELEGRAM_BOT_TOKEN:-${TELEGRAM_BOT_TOKEN:-}}"
fi
[[ -n "$TOKEN" ]] || { echo "No data: token env $TOKEN_ENV empty" >&2; exit 3; }
CHAT="${COUNCIL_CHAT_ID:-}"
if [[ -z "$CHAT" && -f "$ROOT/config/relay.conf" ]]; then
  CHAT=$(grep -E '^COUNCIL_CHAT_ID=' "$ROOT/config/relay.conf" | cut -d= -f2- || true)
fi
[[ -n "$CHAT" ]] || { echo "No data: COUNCIL_CHAT_ID not set in relay.conf" >&2; exit 4; }
python3 - "$TOKEN" "$CHAT" "$TEXT" << 'PY'
import json, sys, urllib.request
token, chat, text = sys.argv[1], sys.argv[2], sys.argv[3][:3900]
req = urllib.request.Request(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data=json.dumps({"chat_id": chat, "text": text, "disable_web_page_preview": True}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=20) as r:
    body = json.load(r)
if not body.get("ok"):
    raise SystemExit(f"send failed: {body}")
print("[ok] posted")
PY
