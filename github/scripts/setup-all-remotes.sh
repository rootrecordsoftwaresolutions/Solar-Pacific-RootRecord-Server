#!/usr/bin/env bash
# Ensure each enabled repo has an authenticated remote. Worktrees under BAK_ROOT.
set -euo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
load_token

remote_url() {
  local slug="$1"
  echo "https://x-access-token:${GITHUB_TOKEN}@github.com/${slug}.git"
}

while IFS=$'\t' read -r id enabled mode local_path slug remote_name; do
  [[ "$id" =~ ^#.*$ || -z "${id:-}" ]] && continue
  [[ "$enabled" != "1" ]] && { echo "[skip] $id disabled"; continue; }

  if [[ "$mode" == "inplace" ]]; then
    root="$local_path"
  else
    root="$BAK_ROOT/worktrees/$id"
    mkdir -p "$root"
    if [[ ! -d "$root/.git" ]]; then
      echo "[clone] $id → $root"
      git clone --depth 1 "$(remote_url "$slug")" "$root" 2>&1 | redact
    fi
  fi

  if [[ ! -d "$root/.git" ]]; then
    echo "[warn] $id: not a git repo at $root — skip remote setup"
    continue
  fi
  cd "$root"
  url="$(remote_url "$slug")"
  if git remote get-url "$remote_name" >/dev/null 2>&1; then
    git remote set-url "$remote_name" "$url"
    echo "[ok] $id updated remote '$remote_name'"
  else
    git remote add "$remote_name" "$url"
    echo "[ok] $id added remote '$remote_name'"
  fi
done < <(grep -v '^#' "$REPOS_CONF" | grep -v '^[[:space:]]*$')
