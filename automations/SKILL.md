---
name: automations
description: >-
  Boot poller + Cloudflare tunnel + jobs.py (incl. github_sync_all every 300s).
  After GitHub pulls new skills code, the stack auto-reloads — do not suggest manual restart.
---

# automations

**MUST:** Ctrl-C / `rootserver-poller stop` kills poller + cloudflared + unit.

## Auto-reload after GitHub pull (automated — do not suggest parallel restarts)

When `github_sync_all` merges remote skills code into the live tree:

1. `push-repo-once.sh` sets `/home/rootrecord/Database/GITHUB/flags/reload-poller-stack`
2. `sync-all.sh` calls `schedule-stack-reload.sh`
3. After an 8s deferral (so the sync job can exit), the stack **fully stops then starts**:
   - `rr-rootserver-poller.service`
   - `rootserver_poller.py`
   - cloudflared tunnel
   - `poller-watch.py`
4. `ava-ecoflow-ble.service` is **not** killed (single BLE owner stays)

**AI operators must not:**
- suggest `/home/rootrecord/rootserver-poller restart` after a code push/pull that will sync naturally;
- start a second poller, second cloudflared, or parallel "apply the new code" process;
- dual-start BLE owners.

Manual restart remains valid only when the operator explicitly wants an immediate reload outside the 5-minute sync window, or when diagnosing a hung stack.

| | |
|--|--|
| Jobs | `scripts/jobs.py` |
| CLI | `/home/rootrecord/rootserver-poller` |
| Public | `https://rootserver.rootrecord.cloud/` |
| GitHub sync | `github_sync_all` → skills + website + mainland |
| Auto-reload | `scripts/schedule-stack-reload.sh` |
| Data | `/home/rootrecord/Database/` (intake + GITHUB baks) |

`ON_BOOT` p0 self → p1 tunnel → p2 `github_setup_remotes` → schedules.
EcoFlow reads: `ONCE_AT_START` + every :00/:15/:30/:45 → SQLite dual-write; `/energy` prefers SQLite.
