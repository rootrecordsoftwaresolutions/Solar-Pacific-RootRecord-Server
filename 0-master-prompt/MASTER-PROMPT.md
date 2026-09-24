# RootRecord Master Prompt

## 1. Purpose

You are working inside the RootRecord ecosystem. This master prompt is the durable cross-project operating contract. It should let a new session orient itself without requiring the operator to re-upload the same context.

Implementation details belong in the actual RootRecord repositories.

This directory also contains a machine-readable live-state layer. The prompt defines how to work; the state files describe what is currently known; the logs preserve the observed timeline.

## 2. Repository map

### Solar Pacific RootRecord Server

https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server

Primary local/server skills, automations, energy, agent lanes, communications, operational state, and RootRecord server-side development.

### US Mainland Server

https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server

AWS/mainland mirror and recovery-oriented infrastructure. The repository is a mirror/recovery source for the mainland system; do not assume every mirrored file is the live deployed state without verification.

### RootRecord Website

https://github.com/rootrecordsoftwaresolutions/RootRecord-Website

Public Next.js website. Current foundation uses Next.js 15, React 19, and TypeScript.

### RootRecord Master Prompt

https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt

Cross-project rules, workflow, durable context, repository/file index, and generated bundle.

## 3. Operating workflow

The standard development loop is:

1. **Inspect** the real current file/path.
2. **Trace** the actual flow involved.
3. **Patch** the existing final path.
4. **Validate** the changed behavior.
5. **Independently double-check** the result.
6. **Hand off** with concise evidence.

Do not stop after writing a file and call it fixed.

## 3b. Deploy format — standing rule for all future builds

**This is permanent policy for Solar Pacific skills deploys. Keep this format for all future builds.**

| Step | What happens |
|------|----------------|
| 1 | Change lands on GitHub `main` |
| 2 | Desk `github_sync_all` (~300s) fetch/merge (no force-push, no hard reset) |
| 3 | Skills merge arms `Database/GITHUB/flags/reload-poller-stack` |
| 4 | `schedule-stack-reload.sh` fully stops then starts the poller stack |
| 5 | New code runs; no parallel “activate” process |

**AIs must not:** recommend default manual poller restart after ordinary pushes; start a second poller/tunnel/BLE owner; invent a competing deploy path.

**AIs must:** preserve this format when adding jobs, energy features, or services; document handoffs so the next agent inherits the same expectation.

Manual restart or full machine reboot only when the operator asks, the stack is hung, or a one-time first load of the automation is needed.

Detail: `handoff/AUTO-STACK-RELOAD-2026-09-24.md`, `automations/scripts/schedule-stack-reload.sh`.

## 4. Live state and telemetry

The live-state layer is part of the operating context.

### Current snapshot

`state/state.json` is the canonical machine-readable snapshot of the latest known state.

It may contain:

- repository/runtime connection status;
- service reachability;
- power and energy readings;
- active work;
- recent worklog information;
- verification timestamps;
- source/provenance for observed values.

The snapshot is expected to refresh on the established five-minute cadence when the state updater is running.

### Historical state

`logs/state-history.json` is the append-oriented machine-readable timeline.

A five-minute refresh may record a snapshot even when nothing changed. This is intentional: the history is a black-box recorder for RootRecord operational continuity, not merely a human-readable changelog.

Do not infer that an old value is current. Every live value must carry a verification timestamp and, where applicable, a source.

### Missing telemetry

Use explicit states such as `unknown`, `stale`, `disconnected`, or `offline` when evidence is unavailable.

Never manufacture a value to make the state look complete.

### Evidence

Live-state claims follow the same evidence discipline as all other operational claims:

- **Confirmed** — directly verified by the recorded source/readback.
- **Hypothesis** — plausible but not independently established.
- **Unknown** — not established.
- **Historical** — true only for a prior checkpoint.

## 5. Existing architecture first

- Reuse existing files, services, operations, and paths.
- Do not create `v2` directories, alternate roots, installers, migrations, or parallel implementations unless explicitly requested.
- Do not rename a final implementation file simply to make a new implementation easier.
- Do not rebuild a system that already has a working operation.
- Trace page → API → handler → data → collector/builder → scheduler/runtime when that chain applies.
- Prefer the smallest surgical change that fits the existing architecture.

The `0-master-prompt` rename is an intentional organizational change, not a new implementation root.

## 6. Operator efficiency

The operator prefers fast, concrete progress over unnecessary questions.

When execution is delegated to the operator:

- Use one paste-safe block per step.
- Use absolute paths.
- Put file writes behind explicit exact-match checks where appropriate.
- Validate after editing.
- Preserve rollback capability.
- Do not make the operator discover an assistant-created bug.

## 7. Safe editing pattern

For consequential edits, prefer:

**exact-match check → backup → edit → verify → automatic/manual rollback if verification fails**

Do not overwrite a file blindly when a bounded edit is sufficient.

## 8. Evidence discipline

Every important claim should be classified:

- **Confirmed**
- **Hypothesis**
- **Unknown**
- **Historical**

A source archive or old handoff is historical evidence unless current state has been verified.

A local agent's assertion is not independent hardware verification.

For live operational claims, the strongest evidence is an operator-run command plus readback/packet/state evidence showing the changed state.

## 9. Temporary files

Disposable troubleshooting helpers do not belong in project/home directories.

For EcoFlow work in particular:

- temporary scripts → `/tmp/`
- permanent action scripts → the established energy skill structure
- do not leave `dig*.sh`, probe, cleanup, or one-off helper debris in `/home/rootrecord/`

## 10. Secrets

Never print, paste, commit, or document token values.

Use environment variable names only when documenting secrets, for example:

- `TELEGRAM_AVA_TOKEN`
- `TELEGRAM_BRUCE_TOKEN`
- `TELEGRAM_CARLY_TOKEN`

Only one .env may be used, located at `/home/rootrecord/master/master-key.env`.

## 11. Durable documentation

Update the master-prompt area when a rule, workflow convention, repository boundary, or durable cross-project decision changes.

Do not copy large implementation files into this repository.

The repository/file index should contain links to the real files instead.

## 12. Handoffs

A handoff should tell the next agent:

- what is current;
- what changed;
- what was actually verified;
- what remains;
- what is historical;
- what the next concrete action is;
- that **deploy remains push → sync → auto full stack reload** for future builds.

Do not create a giant handoff simply because the previous session was long.

## 13. RootRecord architectural context

The foundational context describes RootRecord as an ecosystem centered on:

- constant self and community improvement;
- data stewardship;
- local-first processing where practical;
- resilient infrastructure;
- continuity;
- Representative Intelligence Systems;
- intentional evolution.

The AVA v0.04 architecture remains an active/open design process. Do not silently turn its unresolved questions into finalized requirements.

Current conceptual agent loop:

`AVA → Bruce → Carly → AVA`

This is architectural context, not a license to invent unresolved agent authority, values, memory boundaries, or identity rules.

## 14. Energy/EcoFlow caution

Do not infer device behavior from wrapper names alone.

For EcoFlow actions:

- inspect the underlying implementation;
- distinguish measured values from library defaults;
- account for connection/authentication timing;
- serialize BLE sessions;
- verify that the requested value actually changed;
- keep catalog statuses current after meaningful PASS results.

AC state requires particular care because inverter heartbeat packets and default values can differ from what a wrapper appears to report.

## 15. Public operational surfaces

The RootRecord poller is documented as GET-only/public through its tunnel endpoints.

Do not add an unauthenticated mutation/toggle route.

Do not claim a scheduler feature exists merely because a catalog or template exists. Verify the running scheduler/runtime behavior.

## 16. Historical boundary

Historical work remains valuable, but historical ≠ current.

When a reset, migration, or repository cleanup has occurred:

- current repository contents define current source state;
- old archives remain historical reference;
- a working implementation found only in an archive must not be described as currently deployed until verified.

## 17. Final rule

Do the work, verify the work, and leave the next agent a cleaner understanding than the one you started with.

Preserve the standing deploy format (GitHub → sync → auto full stack reload) in every future build unless the operator explicitly changes policy.
