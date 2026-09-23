#!/usr/bin/env bash
set -euo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
load_token

remote_url() { echo "https://x-access-token:${GITHUB_TOKEN}@github.com/${1}.git"; }

while IFS=$'\t' read -r id enabled mode local_path slug remote_name; do
  [[ "$id" =~ ^#.*$ || -z "${id:-}" ]] && continue
  [[ "$enabled" != "1" ]] && { echo "[skip] $id disabled"; continue; }

  if [[ "$mode" == "inplace" ]]; then
    root="$local_path"
  else
    root="$BAK_ROOT/worktrees/$id"
  fi
  mkdir -p "$(dirname "$root")"

  if [[ ! -d "$root/.git" ]]; then
    if [[ -d "$root" ]] && [[ -n "$(ls -A "$root" 2>/dev/null || true)" ]]; then
      echo "[warn] $id: $root non-empty without .git — fix manually"
      continue
    fi
    echo "[clone] $slug → $root"
    git clone "$(remote_url "$slug")" "$root" 2>&1 | redact
  fi

  cd "$root"
  url="$(remote_url "$slug")"
  if git remote get-url "$remote_name" >/dev/null 2>&1; then
    git remote set-url "$remote_name" "$url"
    echo "[ok] $id remote '$remote_name' updated"
  else
    if [[ "$remote_name" == "origin" ]] && git remote get-url origin >/dev/null 2>&1; then
      git remote set-url origin "$url"
      echo "[ok] $id origin set"
    else
      git remote add "$remote_name" "$url"
      echo "[ok] $id remote '$remote_name' added"
    fi
  fi
done < <(grep -v '^#' "$REPOS_CONF" | grep -v '^[[:space:]]*$')
