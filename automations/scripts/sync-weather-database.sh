#!/usr/bin/env bash
set -euo pipefail

REPO="/home/rootrecord/Database/WEATHER"
REMOTE="origin"
BRANCH="main"
LOCK="/tmp/rootrecord-weather-db-sync.lock"

exec 9>"$LOCK"
flock -n 9 || exit 0

cd "$REPO"

git fetch "$REMOTE" "$BRANCH" --quiet

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
    git add -A
    if ! git diff --cached --quiet; then
        git commit -m "Initial weather database sync"
    fi
    git push -u "$REMOTE" "$BRANCH"
    exit 0
fi

LOCAL_SHA="$(git rev-parse HEAD)"
REMOTE_SHA="$(git rev-parse "$REMOTE/$BRANCH")"

# If GitHub has moved ahead, propagate remote deletions locally
# before merging. This intentionally does NOT use reset --hard.
if [ "$LOCAL_SHA" != "$REMOTE_SHA" ]; then
    BASE="$(git merge-base "$LOCAL_SHA" "$REMOTE_SHA")"

    while IFS= read -r path; do
        [ -n "$path" ] || continue
        rm -rf -- "$REPO/$path"
    done < <(git diff --name-only --diff-filter=D "$BASE" "$REMOTE_SHA")

    git add -A

    if ! git diff --cached --quiet; then
        git commit -m "Sync weather database changes"
    fi

    if ! git merge --no-edit "$REMOTE/$BRANCH"; then
        git merge --abort || true
        echo "Weather database sync: merge conflict; leaving local data untouched."
        exit 1
    fi
fi

git add -A

if ! git diff --cached --quiet; then
    git commit -m "Update weather database"
fi

git push "$REMOTE" "$BRANCH" --quiet
