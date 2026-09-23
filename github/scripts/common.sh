#!/usr/bin/env bash
# Shared paths for github skill — never print tokens.
BAK_ROOT="${BAK_ROOT:-/home/rootrecord/Database/GITHUB}"
ENV_FILE="${ENV_FILE:-/home/rootrecord/master/master-key.env}"
GITHUB_SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOS_CONF="${REPOS_CONF:-$GITHUB_SCRIPTS/repos.conf}"
MAX_FILE_MB="${MAX_FILE_MB:-90}"

ensure_bak_root() {
  mkdir -p "$BAK_ROOT" "$BAK_ROOT/worktrees" "$BAK_ROOT/logs"
}

load_token() {
  if [[ -z "${GITHUB_TOKEN:-}" && -f "$ENV_FILE" ]]; then
    # shellcheck disable=SC1090
    set -a; source "$ENV_FILE"; set +a
  fi
  if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    echo "ERROR: GITHUB_TOKEN missing in $ENV_FILE" >&2
    return 1
  fi
}

redact() {
  sed -E 's#(x-access-token:)[^@]+@#\1***@#g'
}
