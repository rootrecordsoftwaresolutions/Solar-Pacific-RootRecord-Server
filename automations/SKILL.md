---
name: automations
description: >-
  Boot poller + Cloudflare tunnel + jobs.py (github_sync_all every 300s).
  Auto stack reload after skills pull; reopen status window.
  Standing format for all future builds — sectioned jobs.py, no parallel runtimes.
---

# automations

**MUST:** Ctrl-C / close window / `rootserver-poller stop` kills poller + cloudflared + unit.

## HOW TO ADD A JOB

1. Open `scripts/jobs.py`.
2. Copy the **TEMPLATE** block inside the matching **SECTION** (ON_BOOT, EVERY_MINUTE, …).
3. Paste above the TEMPLATE, set `enabled=True`, fill fields, keep key order.
4. Code apply is automatic after GitHub pull (do not invent a second scheduler).

## Auto-reload after GitHub pull (standing)

1. Skills merge arms reload flag + `schedule-stack-reload.sh`
2. `do-stack-reload.sh` stops stack, starts unit, **opens status window**
3. BLE owner (`ava-ecoflow-ble`) is **not** killed

**Do not** suggest default manual restart after ordinary pushes; **do not** dual-start pollers/tunnels/BLE.

## Layout style (standing)

`jobs.py` is the canonical sectioned catalog. Keep SECTION + TEMPLATE blocks.
If missing, restore from git and re-apply live jobs. See `0-master-prompt/prompts/09-file-layout-style.md`.

## Paths

| | |
|--|--|
| Jobs | `scripts/jobs.py` |
| CLI | `/home/rootrecord/rootserver-poller` |
| Public | `https://rootserver.rootrecord.cloud/` |
| Auto-reload | `scripts/schedule-stack-reload.sh` → `do-stack-reload.sh` |
| Data | `/home/rootrecord/Database/` |

`ON_BOOT` p0 self → p1 tunnel (internet gate) → p2 remotes → Ollama/FLM/relay → p6 a-eyes cam server → p7 a-eyes timelapse catch-up.
EcoFlow: ONCE_AT_START + every :00/:15/:30/:45 → SQLite dual-write.
a-eyes timelapse: EVERY_HOUR compiles the hour just ended; ON_AT 22:01 stitches the day + exports the GIF; ON_BOOT catch-up covers any hour missed while the poller was down. Scripts live in the a-eyes skill, not here.
