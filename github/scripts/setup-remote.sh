#!/usr/bin/env bash
# One-time setup: configure a "backup" git remote authenticated with
# GITHUB_TOKEN, without touching your existing "origin" remote.
set -euo pipefail

ENV_FILE="/home/rootrecord/master/master-key.env"
REPO_DIR="/home/rootrecord/.ollama/skills"
REPO_SLUG="rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: env file not found at $ENV_FILE" >&2
  echo "Create it with a single line: GITHUB_TOKEN=ghp_xxxxxxxx" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$ENV_FILE"

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "ERROR: GITHUB_TOKEN is not set inside $ENV_FILE" >&2
  exit 1
fi

cd "$REPO_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: $REPO_DIR is not a git repository" >&2
  exit 1
fi

REMOTE_URL="https://x-access-token:${GITHUB_TOKEN}@github.com/${REPO_SLUG}.git"

if git remote get-url backup >/dev/null 2>&1; then
  git remote set-url backup "$REMOTE_URL"
  echo "Updated existing 'backup' remote."
else
  git remote add backup "$REMOTE_URL"
  echo "Added new 'backup' remote."
fi

echo "Done. 'origin' remote is untouched."
git remote -v | grep -v "x-access-token" || true
echo "(backup remote URL hidden from output on purpose — it contains the token)"
