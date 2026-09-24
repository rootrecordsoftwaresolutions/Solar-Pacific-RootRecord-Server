# Handoff — Automatic poller stack reload after GitHub pull

**Date:** 2026-09-24  
**Audience:** External AIs and operators  
**Status:** Implemented on `main` — **standing format for all future builds**

---

## Standing rule (do not regress)

**Keep this format for every future build, feature, and deploy.**

1. Code lands on GitHub `main` in the skills tree.
2. Desk `github_sync_all` pulls/merges (no force-push, no `reset --hard`).
3. A skills merge arms reload → deferred **full** stop/start of the poller stack.
4. New code loads without a second process, parallel apply script, or default “please restart” instruction.
5. BLE owner stays single-owner (`ava-ecoflow-ble` is not killed by reload).

If you add schedulers, energy jobs, website hooks, or new services: **wire them into this path**, do not invent a parallel restart or dual-runtime pattern.

Breaking this format (second poller, manual-restart-only deploys, dual BLE owners) is a regression unless the operator explicitly requests a different design.

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

## AI rules (mandatory — all future sessions)

1. **Do not** recommend `rootserver-poller restart` after a normal push to `main` that the desk will sync.
2. **Do not** start a second poller, second cloudflared, or parallel "activate code" script.
3. **Do not** dual-start BLE owners.
4. Manual restart is OK only if the **operator asks**, or the stack is **hung** outside the sync window, or they are doing a **full machine reboot**.
5. **Preserve this deploy format** in all future builds: push → sync → auto full stack reload. Document new features so the next agent inherits the same expectation.

---

## Files

| Path | Role |
|------|------|
| `github/scripts/push-repo-once.sh` | Arms reload flag on skills merge |
| `github/scripts/sync-all.sh` | Calls schedule-stack-reload after repos |
| `automations/scripts/schedule-stack-reload.sh` | Deferred full stop/start |
| `automations/scripts/stop-poller-stack.sh` | Existing hard stop |
| `automations/SKILL.md` | Operator/AI summary |
| `0-master-prompt/MASTER-PROMPT.md` | Cross-project standing contract |
| `0-master-prompt/prompts/00-core.md` | No parallel runtime |
| `0-master-prompt/prompts/03-development.md` | Deploy path |
| `0-master-prompt/prompts/04-operations.md` | Ops policy |
| `0-master-prompt/prompts/07-current-state.md` | Current automation note |

---

## Operator note

A full device reboot after the first pull of this automation is fine. After that, further GitHub pushes to skills should self-apply via sync + stack reload without another manual restart. **Future builds keep the same format.**
