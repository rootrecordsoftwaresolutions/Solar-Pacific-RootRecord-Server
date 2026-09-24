# RootRecord Data Layer + Clock-Aligned Sync Upgrade Plan

**Project:** Solar-Pacific-RootRecord-Server  
**Local root:** `/home/rootrecord/.ollama/skills`  
**Canonical database:** `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`  
**Status:** IMPLEMENTATION IN PROGRESS — schema, dual-write, condensation, scheduled EcoFlow reads, auto stack-reload after GitHub pull are on `main`; production DB init + live validation remain operator steps.

---

## 1. Mission

Move RootRecord away from sprawling JSON, growing telemetry logs, filesystem bucket stubs, process-relative timers, and GitHub-tracked runtime artifacts toward:

- SQLite-first **9-layer** time-resolution architecture
- wall-clock-aligned condensation
- safe bidirectional non-destructive GitHub sync
- **automatic full poller stack reload** when skills code is pulled
- LLM-queryable DB skill
- thin Mainland/AWS edge

| Layer | Holds |
|---|---|
| **GitHub** | code, configuration, schemas, skills |
| **SQLite** | canonical live + historical runtime data |
| **JSON** | small config / compatibility snapshots only |
| **Logs** | diagnostics only — never telemetry |
| **Mainland/AWS** | thin, independent deploy/update edge |

---

## 2. Nine-layer model (canonical)

```
1sec → 1min → 5min → 15min → 1hour → day → 7days → month → year
```

**Working (reset after verified condensation):** 1sec, 1min, 5min, 15min, 1hour  
**Permanent (append-only):** day, 7days, month, year

Rules: never fabricate data; missed boundaries self-heal; condensation idempotent.

Timestamps: UTC `Z` storage; Pacific/Honolulu reporting boundaries.

---

## 3. Critical rules

1. SQLite canonical at `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`.
2. GitHub is not a telemetry store.
3. No destructive Git ops.
4. Wall-clock timing, not process uptime.
5. No second BLE owner, poller, scheduler, or sync engine.
6. **Code apply is automated:** GitHub pull of skills → flag → deferred full stack stop/start. AIs must not suggest parallel restarts.

---

## 4. Device model

| Logical | SN | Role |
|---------|-----|------|
| B1 | R621ZA16XH6K1155 | River 2 Pro |
| B2 | R331ZAB5SG6S2858 | Delta 2 |
| B3 | R331ZAB5SG755642 | Expansion under B2 (not separate BLE) |

---

## 5. Built on main

- [x] Schema v2, store, ingest, aggregate/condense, dual-write `read_runner`
- [x] Tooling: init / migrate / verify / condense / latest snapshot
- [x] B3 inventory in `devices.conf`
- [x] Poller jobs: EcoFlow read at boot + every 15 min; `/energy` prefers SQLite
- [x] Auto stack reload after skills code pull (`schedule-stack-reload.sh`)
- [x] Master-prompt + handoff docs for auto-reload (no parallel restart advice)

---

## 6. Still open

1. Production DB init + `verify_rootrecord_db.py` (operator)
2. Live dual-write validation on real BLE
3. Wall-clock condensation hook deeper into existing timers (reads already scheduled)
4. Exact-boundary GitHub sync timing (reload already on pull)
5. Git runtime-artifact cleanup / JSON reduction
6. LLM query interface / Mainland thin edge / full cutover

---

## 7. Deploy note for operators

After pulling this revision, a **one-time device reboot** (or one `rootserver-poller restart`) loads the new automation. Thereafter, GitHub pushes to skills self-apply via sync + stack reload. See `handoff/AUTO-STACK-RELOAD-2026-09-24.md`.
