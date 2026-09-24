---
name: automations
description: >-
  Boot poller + Cloudflare tunnel + jobs.py (incl. github_sync_all every 300s).
  After GitHub pulls new skills code, the stack auto-reloads and reopens the status window.
  Standing format for all future builds — do not suggest manual restart or parallel runtimes.
---

# automations

**MUST:** Ctrl-C / `rootserver-poller stop` kills poller + cloudflared + unit.

## Auto-reload after GitHub pull — standing format for all future builds

**Keep this format for every future build.** Do not invent a competing restart or dual-runtime path.

When `github_sync_all` merges remote skills code into the live tree:

1. `push-repo-once.sh` sets reload flag and runs `schedule-stack-reload.sh`
2. After ~8s, `do-stack-reload.sh`:
   - stops unit + poller + cloudflared + poller-watch
   - starts `rr-rootserver-poller.service`
   - **reopens the status window** (`open-poller-window.sh`)
3. `ava-ecoflow-ble.service` is **not** killed

**AI operators must not:** suggest default manual restart after ordinary pushes; start a second poller/tunnel/BLE owner; regress this format.

| | |
|--|--|
| Jobs | `scripts/jobs.py` |
| CLI | `/home/rootrecord/rootserver-poller` |
| Public | `https://rootserver.rootrecord.cloud/` |
| GitHub sync | `github_sync_all` → skills + website + mainland |
| Auto-reload | `schedule-stack-reload.sh` → `do-stack-reload.sh` (includes window) |
| Data | `/home/rootrecord/Database/` |
