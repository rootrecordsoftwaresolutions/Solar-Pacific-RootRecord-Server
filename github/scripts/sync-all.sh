#!/usr/bin/env bash
# One cycle for every enabled repo in repos.conf
set -uo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RC=0
while IFS=$'\t' read -r id enabled mode local_path slug remote_name; do
  [[ "$id" =~ ^#.*$ || -z "${id:-}" ]] && continue
  [[ "$enabled" != "1" ]] && continue
  if ! bash "$SCRIPTS/push-repo-once.sh" "$id"; then
    RC=1
  fi
done < <(grep -v '^#' "$REPOS_CONF" | grep -v '^[[:space:]]*$')
exit $RC
