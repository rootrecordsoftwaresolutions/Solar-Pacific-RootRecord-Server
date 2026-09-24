# Handoff — Automatic poller stack reload after GitHub pull

**Date:** 2026-09-24  
**Audience:** External AIs and operators  
**Status:** Implemented on `main`

---

## What this is

When new skills code is **pulled/merged from GitHub** into the live desk tree, the RootRecord poller stack **fully stops and starts itself**. Operators and AIs do not need to restart the poller for ordinary deploys.

---

## Flow (confirmed)

```
github_sync_all (jobs.py, ~every 300s)
  → github/scripts/sync-all.sh
    → github/scripts/push-repo-once.sh  (per repo)
         if GitHub commits merge into skills tree:
           write Database/GITHUB/flags/reload-poller-stack
    → automations/scripts/schedule-stack-reload.sh
         wait ~8s (sync job can exit)
         stop-poller-stack.sh
           · systemctl --user stop rr-rootserver-poller.service
           · kill rootserver_poller.py, cloudflared, poller-watch.py
         clear stale /tmp/ecoflow-ble.lock (action flock only)
         systemctl --user start rr-rootserver-poller.service
         (CLI fallback: /home/rootrecord/rootserver-poller start)
```

**Not stopped:** `ava-ecoflow-ble.service` / BLE owner (must remain single-owner).

**Guards:** single-flight lock, 60s debounce, deferred execution (no parallel apply process).

---

## AI rules (mandatory)

1. **Do not** recommend `rootserver-poller restart` after a normal push to `main` that the desk will sync.
2. **Do not** start a second poller, second cloudflared, or parallel "activate code" script.
3. **Do not** dual-start BLE owners.
4. Manual restart is OK only if the **operator asks**, or the stack is **hung** outside the sync window, or they are doing a **full machine reboot** (as planned after this deploy).

---

## Files

| Path | Role |
|------|------|
| `github/scripts/push-repo-once.sh` | Arms reload flag on skills merge |
| `github/scripts/sync-all.sh` | Calls schedule-stack-reload after repos |
| `automations/scripts/schedule-stack-reload.sh` | Deferred full stop/start |
| `automations/scripts/stop-poller-stack.sh` | Existing hard stop |
| `automations/SKILL.md` | Operator/AI summary |
| `0-master-prompt/prompts/00-core.md` | No parallel runtime |
| `0-master-prompt/prompts/03-development.md` | Deploy path |
| `0-master-prompt/prompts/04-operations.md` | Ops policy |
| `0-master-prompt/prompts/07-current-state.md` | Current automation note |

---

## Operator note for this deploy

A full device reboot after the next pull is fine and will load this automation cleanly. After that, further GitHub pushes to skills should self-apply via sync + stack reload without another manual restart.
