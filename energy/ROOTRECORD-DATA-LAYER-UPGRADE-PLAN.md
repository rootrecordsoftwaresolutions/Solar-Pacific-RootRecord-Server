# RootRecord Data Layer + Clock-Aligned Sync Upgrade Plan

**Project:** Solar-Pacific-RootRecord-Server  
**Local root:** `/home/rootrecord/.ollama/skills`  
**Canonical database:** `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`  
**Status:** IMPLEMENTATION IN PROGRESS — schema, ingestion, dual-write producer, condensation, and tooling are on `main`; production DB init and live cutover remain explicit operator actions.

---

## 1. Mission

Move RootRecord away from sprawling JSON, growing telemetry logs, filesystem bucket stubs, process-relative timers, and GitHub-tracked runtime artifacts toward:

- SQLite-first **9-layer** time-resolution architecture
- wall-clock-aligned condensation
- safe bidirectional non-destructive GitHub sync
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

Rules (non-negotiable):
- Never fabricate data (missing stays missing; measured zero is allowed).
- Missed boundaries self-heal from persisted data on next boot/run.
- Condensation is idempotent.
- Do not discard lower-layer source until upper layer is verified.

Timestamps: observations stored as UTC ISO-8601 with `Z`. Reporting boundaries use Pacific/Honolulu.

---

## 3. Critical rules

1. SQLite is canonical at `/home/rootrecord/Database/ROOTRECORD/rootrecord.db` (see `energy/db/store.py`).
2. GitHub is not a telemetry store.
3. No destructive Git ops (`reset --hard`, force-push).
4. All condensation/sync timing is wall-clock, not process uptime.
5. Do not create a second BLE owner, poller, scheduler, or sync engine.

---

## 4. Device model (locked)

| Logical | SN | Role |
|---------|-----|------|
| B1 | R621ZA16XH6K1155 | River 2 Pro — top-level device |
| B2 | R331ZAB5SG6S2858 | Delta 2 — top-level device |
| B3 | R331ZAB5SG755642 | Expansion battery under B2 (not a separate BLE device) |

`devices.conf` records B3 under `[delta2]` (`expansion_expected_sn`) and `[inventory]`. No MAC is invented for B3. Live discovery is via eflib `battery_*_sn` when the pack is attached to B2.

If B3 is ever a standalone second Delta 2, add a full `[delta2_secondary]` section with a real `mac=` and `eflib_module=` — never invent a MAC.

---

## 5. What is already built (verified on main)

- [x] Canonical schema v2 (`energy/db/schema.sql`) — device, battery (primary+expansion), ports, observations, typed measurements with measured/defaulted/missing/not_applicable, aggregation runs, aggregate metrics including duration/coverage fields
- [x] Persistence primitives (`store.py`)
- [x] EFLIB → SQLite ingest (`ingest.py`) including expansion batteries and ports
- [x] Condensation engine (`aggregate.py` / `condense.py`) — closed-period, idempotent, boundary-aware power integration (60s ceiling), port aggregation
- [x] Dual-write producer (`lib/read_runner.py`) — persist + condense, then legacy JSON compatibility output
- [x] Tooling: `init_rootrecord_db.py`, `migrate_json.py`, `condense_closed_periods.py`, `verify_rootrecord_db.py`, `backfill_legacy_energy.py`
- [x] Regression tests for zero/missing/boundary/gap/idempotency
- [x] Bidirectional GitHub sync present (do not rebuild); telemetry not to be committed
- [x] BLE owner and action scripts preserved
- [x] B3 expansion inventory documented in `devices.conf` (expected SN + parent; no invented MAC)

---

## 6. What still needs to continue being built

Ordered; each step is inspect-then-change.

1. ~~Close config inventory gap~~ **done** — B3 documented as expansion under B2; no MAC invented.

2. **Production DB initialization (operator)**  
   Initialize empty DB at the canonical path; run verifier. No mass import required unless explicitly chosen.

   ```bash
   cd /home/rootrecord/.ollama/skills
   energy/lib/py -m energy.scripts.init_rootrecord_db
   # or: energy/lib/py energy/scripts/init_rootrecord_db.py
   energy/lib/py energy/scripts/verify_rootrecord_db.py
   ```

3. **Live dual-write validation**  
   Real BLE reads of `delta2` and `river2pro` → confirm observation counts, state semantics, expansion-battery rows when B3 is attached, condensation of closed periods. Keep legacy JSON until verified.

   ```bash
   energy/scripts/read/delta2-read.sh
   energy/scripts/read/river2pro-read.sh
   ```

4. **Wall-clock scheduler integration**  
   Hook condensation (and any remaining timing) into existing poller/timers. No competing scheduler.

5. **Exact-boundary GitHub sync**  
   Align existing sync to clock boundaries; ensure no runtime telemetry/logs/DBs enter Git.

6. **Git runtime-artifact cleanup**  
   Inventory tracked logs/JSON/runtime paths → migrate off → `git rm --cached` → harden `.gitignore`.

7. **JSON reduction**  
   Classify ~889 files under `Database/`; keep / migrate / generate / delete with explicit labels. No mass conversion.

8. **Optional historical backfill**  
   Only if product decision is to import legacy JSON/DB samples; tooling exists, remains operator-triggered.

9. **Read-only LLM query interface** on SQLite.

10. **Thin Mainland/AWS updater**.

11. **Failure/rollback pass + production cutover**  
    Documented rollback for every destructive step; retire legacy writers only after independent verification.

---

## 7. Explicit non-goals (do not do)

- Second BLE owner / poller / scheduler / sync engine
- Importing historical EcoFlow DBs by default (inspect-only unless decided otherwise)
- Treating `energy/data/` as the production DB path (superseded by code)
- Fabricating missing values or inventing BLE MACs
- Enabling aggressive poll buckets while dual-write validation is incomplete
- Force-push or hard-reset in any sync path

---

## 8. Definition of done

1. BLE telemetry no longer lives only in growing Git-tracked logs.
2. All runtime telemetry lives in SQLite under the 9-layer model.
3. Each layer condenses on correct wall-clock boundaries with missed-boundary self-heal.
4. Missing data is never fabricated.
5. Backfill (if used) is idempotent.
6. GitHub sync runs on exact clock boundaries and never carries telemetry.
7. JSON sprawl is classified and reduced.
8. LLMs can query the DB read-only.
9. Existing RootRecord functionality remains intact.
10. Mainland can update independently from GitHub.
11. No destructive Git operation in the pipeline.
12. Every migration step has a documented rollback.

---

## 9. Checkpoint

Code on `main` implements schema, dual-write ingestion, condensation, verification tooling, and B3 inventory in config. Production database initialization and full live cutover have **not** been claimed complete.

Canonical DB path (code): `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`

**Next operator action:** init + verify DB, then live dual-write reads.

Still open after that: wall-clock scheduler integration, exact-boundary Git sync, Git runtime cleanup, JSON reduction, LLM query interface, Mainland edge, full cutover.

Preserve BLE owner and existing sync. Do not treat historical EcoFlow DBs as import sources unless explicitly decided.
