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
4. After start, the **status window is reopened** (`open-poller-window.sh`).
5. BLE owner stays single-owner (`ava-ecoflow-ble` is not killed by reload).

If you add schedulers, energy jobs, website hooks, or new services: **wire them into this path**, do not invent a parallel restart or dual-runtime pattern.

---

## Flow (confirmed)

```
github_sync_all (jobs.py, ~every 300s)
  → github/scripts/sync-all.sh / push-repo-once.sh
         merge skills → flag + schedule-stack-reload.sh
    → do-stack-reload.sh (~8s later)
         stop-poller-stack.sh
         systemctl --user start rr-rootserver-poller.service
         open-poller-window.sh   # desired: window comes back
```

**Guards:** single-flight lock, debounce, systemd-run or nohup/setsid, user D-Bus + DISPLAY for window.

---

## AI rules (mandatory — all future sessions)

1. **Do not** recommend `rootserver-poller restart` after a normal push to `main` that the desk will sync.
2. **Do not** start a second poller, second cloudflared, or parallel "activate code" script.
3. **Do not** dual-start BLE owners.
4. Manual restart is OK only if the **operator asks**, or the stack is **hung** outside the sync window, or they are doing a **full machine reboot**.
5. **Preserve this deploy format** in all future builds (including window reopen).

---

## Files

| Path | Role |
|------|------|
| `github/scripts/push-repo-once.sh` | Arms + schedules reload on skills merge |
| `github/scripts/sync-all.sh` | Backup schedule at end of sync |
| `automations/scripts/schedule-stack-reload.sh` | Deferred trigger |
| `automations/scripts/do-stack-reload.sh` | Stop + start + **open window** |
| `automations/scripts/stop-poller-stack.sh` | Hard stop |
| `automations/scripts/open-poller-window.sh` | Status window |
