# Core Rules

## Work style

- Work quickly, but do not skip verification.
- Inspect before modifying.
- Reuse the existing architecture.
- Make the smallest change that solves the actual problem.
- Avoid unnecessary questions when the repository/source can answer the question.

## Required loop

**inspect → patch → validate → independently double-check → hand off**

## Evidence

Use:

- **Confirmed**
- **Hypothesis**
- **Unknown**
- **Historical**

Never upgrade a hypothesis to confirmed merely because it sounds plausible.

## Operator protection

The operator should not have to discover assistant mistakes.

If you make a change, verify it yourself before handing it back.

## No duplicate architecture

Do not create:

- v2 directories;
- alternate roots;
- duplicate services;
- parallel scripts;
- unnecessary installers;
- migrations;
- renamed copies of the real final file.

Use the existing final path.

## Deploy format — standing rule for all future builds

**Keep this format forever unless the operator explicitly changes policy:**

1. Push to GitHub `main` (skills / existing repos).
2. Desk `github_sync_all` merges (never force-push / never `reset --hard`).
3. Skills merge → automatic **full** poller stack stop/start (`schedule-stack-reload.sh`).
4. No second poller, second cloudflared, second BLE owner, or parallel “apply code” process.
5. Do not default to “please restart the poller” after ordinary pushes.

New features, jobs, energy paths, and services must fit this path. Do not invent a competing deploy or restart scheme.

## No parallel runtime

Do not start a second poller, second cloudflared, second BLE owner, or parallel "apply code" process.

Code pushed to GitHub is applied by the existing `github_sync_all` → merge → **automatic full poller stack reload**. Do not recommend manual restart after ordinary pushes unless the operator asks or the stack is hung.

## Temporary work

Disposable helpers go in `/tmp/`, not project/home directories.
