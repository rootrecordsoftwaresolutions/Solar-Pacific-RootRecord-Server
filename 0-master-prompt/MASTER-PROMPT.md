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

## 3a. File layout style (standing — all AIs)

Operator-facing schedules and catalogs must stay **sectioned and templated**, not compacted.

Canonical example: `automations/scripts/jobs.py`

- `# SECTION:` banners for ON_BOOT, ONCE_AT_START, EVERY_*, ON_AT, etc.
- Commented **TEMPLATE** blocks at the end of each section for copy-paste.
- Header **HOW TO ADD A JOB** (or equivalent).
- New live jobs go **above** the TEMPLATE; do not delete templates to “clean up.”

If you open a file that should look like that and the layout is missing: **restore it** from git history, re-apply live entries, then continue the task.

Full rules: `prompts/09-file-layout-style.md`.

## 3b. Deploy format — standing rule for all future builds

**This is permanent policy for Solar Pacific skills deploys. Keep this format for all future builds.**

| Step | What happens |
|------|----------------|
| 1 | Change lands on GitHub `main` |
| 2 | Desk `github_sync_all` (~300s) fetch/merge (no force-push, no hard reset) |
| 3 | Skills merge arms reload + schedules stack reload |
| 4 | Full stop of poller stack, start unit, **reopen status window** |
| 5 | New code runs; no parallel “activate” process |

**AIs must not:** recommend default manual poller restart after ordinary pushes; start a second poller/tunnel/BLE owner; invent a competing deploy path.

Detail: `handoff/AUTO-STACK-RELOAD-2026-09-24.md`.

## 4. Live state and telemetry

The live-state layer is part of the operating context.

### Current snapshot

`state/state.json` is the canonical machine-readable snapshot of the latest known state.

### Historical state

`logs/state-history.json` is the append-oriented machine-readable timeline.

### Evidence labels

- **Confirmed** — directly verified.
- **Hypothesis** — plausible but not established.
- **Unknown** — not established.
- **Historical** — true only for a prior checkpoint.

## 5. Existing architecture first

- Reuse existing files, services, operations, and paths.
- Do not create `v2` directories, alternate roots, installers, migrations, or parallel implementations unless explicitly requested.
- Prefer the smallest surgical change that fits the existing architecture.

## 6. Operator efficiency

The operator prefers fast, concrete progress over unnecessary questions.

When execution is delegated to the operator: one paste-safe block per step; absolute paths; validate after editing.

## 7. Safe editing pattern

**exact-match check → backup → edit → verify → rollback path if verification fails**

## 8. Secrets

Never print, paste, commit, or document token values. Only one env file: `/home/rootrecord/master/master-key.env`.

## 9. Handoffs

Include: what is current; what changed; what was verified; what remains; that deploy remains push → sync → auto stack reload; that file layout stays sectioned/templated.

## 10. Final rule

Do the work, verify the work, and leave the next agent a cleaner understanding than the one you started with.

Preserve **sectioned file layout** and **auto stack reload deploy** unless the operator explicitly changes policy.
