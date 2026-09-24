# RootRecord Data Layer + Clock-Aligned Sync Upgrade Plan

**Project:** Solar-Pacific-RootRecord-Server
**Local root:** `/home/rootrecord/.ollama/skills`
**Database root:** `/home/rootrecord/Database`
**Status:** IMPLEMENTATION IN PROGRESS — canonical schema, ingestion, aggregation, condensation, migration tooling, and sync foundation are built; production DB remains intentionally uninitialized.

---

## 1. Mission

Move RootRecord away from:

- sprawling JSON state/history files
- continuously growing telemetry logs
- filesystem bucket stubs
- process-relative timers
- GitHub-tracked runtime artifacts

and toward:

- a **SQLite-first, 9-layer time-resolution data architecture**
- a **wall-clock-aligned condensation scheduler**
- a **safe, bidirectional, non-destructive GitHub sync**
- an **LLM-queryable database skill**
- a **thin, independently-updatable Mainland/AWS edge**

Division of responsibility:

| Layer | Holds |
|---|---|
| **GitHub** | code, configuration, schemas, skills |
| **SQLite** | canonical live + historical runtime data |
| **JSON** | small config / compatibility snapshots only |
| **Logs** | diagnostics only — never telemetry |
| **Mainland/AWS** | thin, independent deploy/update edge |

---

## 2. The Corrected Data Model (supersedes earlier bucket design)

This is **not** a generic multi-bucket aggregation system. It is **9 rolling, condensing data layers**, each with an explicit reset/condensation boundary. This replaces any earlier schema built around generic `bucket_data` tables.

```
1sec → 1min → 5min → 15min → 1hour → day → 7days → month → year
```

**9 persistent data layers/files, in order — split into working and permanent tiers:**

**Working / resetting layers** (continuously overwritten, not permanent history):
1. **1sec** — primary/high-resolution layer. Continuously receives raw measurements.
2. **1min** — condensed from 1sec every minute; 1sec resets after condensation.
3. **5min**
4. **15min**
5. **1hour**

**Permanent historical layers** (never reset, only appended to):
6. **day** — condensed at the 24-hour boundary from the working layers.
7. **7days** — condensed weekly average of the `day` layer.
8. **month**
9. **year**

Do not substitute this set with a generic period list (`1m/30m/12h/1d/1w/1mo`, etc.) and do not invent additional permanent aggregation layers beyond these nine.

### Condensation boundaries

- **1sec → 1min:** every minute boundary. 1sec layer clears after condensing.
- **1min/5min/15min/1hour → day:** at the 24-hour boundary.
- **day → 7days:** at **Sunday 23:59**. If the system was offline/unavailable at that boundary, the condensation runs on the **first Monday boot** instead.
- **7days → month, month → year:** same "condense on boundary, or on first boot after a missed boundary" principle applies up the hierarchy.

### Non-negotiable rules for this model

- **Never fabricate data.** A missing measurement stays `missing` — never `0`, never interpolated, unless zero was an actual measured value.
- **Missed boundaries must self-heal.** If the machine was asleep, offline, or crashed through a condensation boundary, the next boot performs the missed condensation from persisted data — not from scheduler memory.
- **Condensation is idempotent.** Running it twice must never double-count or duplicate.
- **Preserve rollback.** Don't discard a lower layer's source data until the layer above it is verified.

---

## 3. Critical Rules (still apply)

### 3.1 SQLite is canonical
Target file: `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`
Exact schema is finalized only after real Energy/BLE payloads are inspected against the 9-layer model above.

### 3.2 GitHub is not a telemetry database
GitHub must never receive: BLE heartbeats, live telemetry, large runtime logs, generated historical JSON, SQLite databases, or disposable runtime state. GitHub stays a code/config/schema layer only.

### 3.3 No destructive Git sync
Never: `git reset --hard origin/main`, `git push --force`.

Required flow:
```
local changes → commit → fetch → compare histories → merge if needed → push
```
Merge conflicts must abort safely, never overwrite.

### 3.4 Exact wall-clock timing
All condensation and sync timing is based on **clock boundaries**, not process uptime (e.g. `xx:05`, `xx:15`, `00:00`, Sunday 23:59, first-of-month 00:00) — not "5 minutes after the process started."

---

## 4. Audit Findings To Date (2026-09-24)

- **No RootRecord canonical DB exists yet.** Unrelated SQLite files exist elsewhere (`unsorted/.../index.sqlite`, `usda.sqlite`) — do not repurpose them.
- **`Database/ENERGY/`** bucket folders (`1m/5m/15m/30m/hour/daily`) are explicitly marked **STUB ONLY**; `poll_enabled=0`. Nothing live is being produced yet — safe to redesign before any data starts flowing.
- **JSON sprawl:** 889 files, ~38 MB, under `Database/`. Needs per-file classification (config / snapshot / history / cache / generated) before any migration — no mass conversion.
- **Logging is a bigger problem than the original BLE log complaint:**
  - `ava-core-session-2026-09-17.log` ≈ 793 MB
  - `ava-core-2026-09-17.log` ≈ 1.52 GB
  - `origin-uvicorn-2026-09-17.log` ≈ 25 MB
  - `ava-console.log` ≈ 21 MB, `ollama.log` ≈ 2.6 MB, `auto-push.log` ≈ 2.1 MB, `rootserver-poller.log` ≈ 1.3 MB
  - Duplicate historical copies live under `~/.ollama/github-history/`, `~/.ollama/old skills/`, `Database/GITHUB/` (the latter alone ≈ 1.3 GB, mostly backups — must not be treated as live data).
- **BLE has many writers/readers** tied to the old log path — all must migrate together: `enable-ble-boot.sh`, `ble-status.sh`, `ble-owner.py`, `ble-log-watch.sh`, `action_runner.py`, `paths.py`, `read_runner.py`, `energy/SKILL.md`, `devices.conf`.
- **`ava-auto-push.timer` exists and is enabled** — unaudited. Must be understood (what it triggers, frequency, overlap with `github_sync_all`, whether it commits runtime artifacts) before any GitHub timing changes.
- **GitHub bidirectional sync (`push-repo-once.sh`) is already built and tested** — do not rebuild. Verified across `skills`, `website`, `mainland` repos.
- **Existing scheduler processes** (`rootserver_poller.py`, `poller-watch.py`) are already running — the wall-clock capability should be integrated into them, not replaced by a competing scheduler.

---

## 5. Mandatory Pre-Migration Repository Audit

**Core rule: understand first, modify second.** Nothing below is a destructive action — this whole phase is read-only inventory. Repository: [Solar-Pacific-RootRecord-Server](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server) (`main` branch, treated as authoritative — not search-engine indexing).

### 5.1 Inspection order
1. **Master control / intent** — `0-master-prompt/`, `handoff/`, `.github/`, `.gitignore`: existing migration plans, operational rules, deployment expectations, CI/CD behavior.
2. **Core runtime** — `agents/`, `automations/`, `coms/`, `plumbing/`: for every script/service found, what launches it, what it reads/writes, whether it's scheduled, whether it touches telemetry or Git, whether its timing is process-relative or wall-clock.
3. **Energy system (high priority)** — the entire `energy/` tree, not just the obvious bucket files: `scripts/poll/`, `scripts/ble/`, `lib/`, `config/`, `buckets/`, `samples/`, `ports/`, `soc/`, `watts/`, `SKILL.md`. Trace the full path: `physical source → BLE/poller → parser → ingestion → storage → aggregation → consumer`. Don't assume a directory's name describes its actual runtime behavior.
4. **GitHub sync** — entire `github/` tree: every pull/fetch/merge/commit/push mechanism, `push-repo-once.sh`, `github_sync_all`, Git timers/hooks, whether any of it currently pushes telemetry/logs/runtime state/databases.
5. **Automation/scheduling** — entire `automations/` tree: search for `interval`, `interval_sec`, `sleep`, `next_due`, `schedule`, `timer`, `cron`, `wall_clock`, `ON_AT`, `systemd`, `poll`, `heartbeat`, `every`, `period`, `bucket`. Classify each as process-relative, wall-clock, systemd-triggered, cron-triggered, Python-internal, or duplicated across multiple schedulers.
6. **State / status / reports** — `state/`, `status/`, `reports/`: classify every persistent file individually (config, current state, historical state, generated report, cache, compatibility snapshot, telemetry, health info). Don't assume every JSON file is disposable.
7. **Logging** — `logs/`: what produces each log, whether it's Git-tracked, whether anything actually consumes it, whether any log is functioning as an accidental database. Do not delete or truncate anything.
8. **Full repository sweep** — after the priority directories, inspect the entire tree for coverage (scripts, config, services, timers, docs, JSON/YAML/TOML, DB references, hidden files, files referenced by code but living outside the obvious subsystem).
9. **Local `/home/rootrecord/Database`** — audited separately when local filesystem access is available: `Database/ENERGY/`, `Database/GITHUB/`, existing SQLite files, JSON collections, historical copies, duplicate archives. Existing Energy structures are not automatically the final architecture.

### 5.2 For every file considered for change
- **Inbound:** what calls/imports/reads/launches/references it?
- **Outbound:** what does it call/import/write/launch/modify?
- **Runtime owner:** what service/process actually executes it?
- **Persistence impact:** what data does changing it affect?
- **Git impact:** could changing it alter sync behavior?

A file isn't safe to replace just because another file looks like it does the same thing.

### 5.3 File classification
Every relevant persistent file eventually gets one label: `CANONICAL_CONFIG`, `CANONICAL_RUNTIME_STATE`, `CANONICAL_TELEMETRY`, `HISTORICAL_DATA`, `GENERATED`, `CACHE`, `DIAGNOSTIC_LOG`, `COMPATIBILITY`, `LEGACY`, or `UNKNOWN`. Nothing marked `UNKNOWN` gets deleted or migrated until its purpose is established.

### 5.4 Explicitly forbidden during the audit
No deleting, renaming, moving, or rewriting files; no replacing schedulers, BLE ingestion, or telemetry paths; no migrating or deleting data (JSON, logs, historical); no initializing a DB over existing data; no changing Git remotes/branches; no `git reset --hard`, `git push --force(-with-lease)`, or `git clean -fd`; no enabling previously-disabled polling or new production timers; no altering production/Mainland deployment behavior. If local and remote repo state differ, report the difference — don't silently resolve it.

### 5.5 Don't build a second competing system
No second poller, scheduler, GitHub sync engine, BLE pipeline, telemetry database, or bucket hierarchy. Existing components get integrated, deliberately replaced, or deliberately retired — never duplicated alongside.

### 5.6 Audit deliverable
Before any implementation starts, produce: (A) repository map, (B) runtime map — what runs and what launches it, (C) telemetry map — source → ingestion → storage → aggregation → consumer, (D) scheduling map, (E) Git sync map, (F) storage map with classifications, (G) dependency map, (H) migration map per component (`KEEP` / `MODIFY` / `REPLACE` / `MIGRATE` / `RETIRE` / `INVESTIGATE` — classifications, not commands), (I) risk list (destructive-op risks, duplicate schedulers/pipelines, data-loss risks, race conditions, missing-boundary risks, Git risks, stale paths, unknown dependencies), (J) nine-layer mapping — for every current telemetry mechanism, which of the nine layers (section 2) it maps to, or `UNMAPPED` if none.

### 5.7 Implementation gate
Move from audit to migration only once: the inventory is complete, runtime ownership is understood, telemetry flow is understood, existing schedulers and Git sync are identified, storage is classified, the nine-layer mapping is done, unknown dependencies are resolved, destructive operations are explicitly excluded, and the migration sequence is documented. The first real implementation step should be the **smallest reversible change** that establishes the new architecture.

---

## 6. Outstanding Diagnostic Commands (read-only, run on the machine itself)

```bash
systemctl --user cat ava-auto-push.timer 2>/dev/null || true
systemctl --user cat ava-auto-push.service 2>/dev/null || true
systemctl --user cat ava-ecoflow-ble.service 2>/dev/null || true
systemctl --user cat rr-rootserver-poller.service 2>/dev/null || true

echo; echo "=== ALL ROOTRECORD TIMERS ==="
systemctl --user list-timers --all 2>/dev/null \
  | grep -Ei 'ava|rr-|rootrecord|energy|poll|push|publish|ingest' || true

echo; echo "=== GIT-TRACKED LOGS ==="
cd /home/rootrecord/.ollama/skills
git ls-files | grep -Ei '(^|/)(logs?|.*\.log$)' | head -300

echo; echo "=== GIT-TRACKED JSON ==="
git ls-files | grep -Ei '\.json$' | head -300

echo; echo "=== GITIGNORE ==="
cat .gitignore

echo; echo "=== ENERGY POLL CODE ==="
find energy/scripts/poll energy/lib energy/scripts/ble \
  -maxdepth 3 -type f -print 2>/dev/null | sort

echo; echo "=== CURRENT SCHEDULER DEFINITIONS ==="
grep -RIn --exclude-dir=.git \
  'interval_sec\|next_due\|ON_AT\|wall_clock\|schedule' \
  automations/scripts 2>/dev/null | head -400
```

This is purely diagnostic — nothing is modified.

---

## 7. Implementation Order

```
1. Repository audit (section 5) + diagnostic commands (section 6)
2. Source data inventory (Energy/BLE payloads, JSON files, logs)
3. Finalize 9-layer schema against real payloads
4. Build database skill (schema, lib, scripts)
5. Initialize empty DB — no producer changes yet
6. BLE → DB migration (structured insert replaces log append)
7. Dual-write validation (old path + DB, compare)
8. Cut BLE fully over to DB
9. Git runtime-artifact cleanup (inventory → migrate → git rm --cached → .gitignore)
10. Build the condensation engine (1sec→1min→...→year, per section 2)
11. Historical backfill (from earliest real data → present, idempotent)
12. Wall-clock scheduler integrated into existing poller
13. Move GitHub sync to exact clock boundaries
14. JSON reduction (classify all 889 files → keep/migrate/generate/delete)
15. Read-only LLM query interface onto the DB
16. Thin Mainland/AWS updater
17. Full failure/rollback test pass
18. Production cutover
```

**Rule for every step above:** inspect before implementing. Nothing in this plan is assumed correct until it's been checked against the actual repository, running processes, and real data.

---

## 8. Rollback Requirements

Before any destructive step:
- Git commit
- DB backup
- config backup
- source-data backup
- migration marker

Never delete original source data until: migration is verified, queries against the new layer are verified, the live producer is verified, and a rollback path is confirmed to work.

---

## 9. Current Status

- [x] GitHub repos reconciled; bidirectional sync built and tested
- [x] Local data-layer audit completed (Energy stubs, BLE dependency chain, log volume, JSON volume)
- [x] Bucket model corrected to the 9-layer condensing architecture, working vs. permanent tiers (section 2)
- [x] Formal pre-migration audit protocol defined (section 5)
- [x] Repository/data-layer audit completed for the implementation scope; remaining live-system checks are operational validation, not schema blockers
- [x] Schema finalized against the inspected EFLIB/EcoFlow model; further fields are additive as new payloads expose them
- [x] Database skill built (`energy/db/` + operational scripts)
- [ ] BLE → DB migration
- [ ] Git runtime cleanup
- [x] Condensation engine implemented with wall-clock boundaries, idempotent runs, boundary-aware power integration, and port aggregation
- [x] Historical backfill tooling implemented; production migration remains an explicit operator action
- [ ] Wall-clock scheduler
- [ ] Exact-boundary GitHub sync
- [ ] JSON reduction
- [ ] LLM query interface
- [ ] Mainland thin edge
- [ ] Production validation

---

## 10. Implementation Checkpoint\n\nImplemented on `main`:\n\n- Canonical SQLite schema separates device identity, primary/expansion batteries, ports, observations, typed measurements, raw/source metadata, and aggregation runs.\n- EcoFlow EFLIB snapshots persist into SQLite while retaining legacy JSON compatibility output.\n- Delta 2 expansion batteries remain children of the Delta 2 device; B3 is not modeled as a separate device.\n- Aggregation uses Honolulu wall-clock boundaries and UTC storage timestamps.\n- Power energy uses bounded trapezoidal integration and now includes valid edge samples across period boundaries without contaminating period statistics.\n- Port telemetry is included in aggregate output.\n- Condensation backfills every closed period between the earliest and latest persisted observations and skips completed periods.\n- Regression coverage exists for edge energy, measured zero, and port aggregation.\n- GitHub synchronization is now race-safe and bidirectional; production telemetry is not committed to GitHub.\n\nProduction DB initialization and live BLE cutover are intentionally not claimed complete until explicitly run and verified.\n\n## 11. Definition of Done

1. BLE telemetry no longer lives in a Git-tracked growing log.
2. All runtime telemetry lives in SQLite, structured per the 9-layer model.
3. Each of the 9 layers condenses on its correct wall-clock boundary, with missed-boundary self-healing.
4. Missing data is never fabricated.
5. Backfill is idempotent.
6. GitHub sync runs on exact clock boundaries and never carries telemetry.
7. JSON sprawl is classified and reduced.
8. LLMs can query the DB directly, read-only.
9. Existing RootRecord functionality is intact throughout.
10. Mainland can update independently from GitHub.
11. No destructive Git operation exists anywhere in the pipeline.
12. Every migration step has a documented rollback.
