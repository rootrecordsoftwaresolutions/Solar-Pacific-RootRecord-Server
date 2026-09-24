# RootRecord Master Prompt

## Purpose

You are working within the RootRecord software ecosystem. This document is the top-level operating contract for agents working across its repositories.

## Source-of-truth hierarchy

When information conflicts, determine its status before acting:

1. **LIVE VERIFIED** — directly observed in the current repository/server/tool output.
2. **DOCUMENTED POLICY** — an explicit current rule in the applicable repository or master-prompt documentation.
3. **HISTORICAL** — older handoffs, transcripts, snapshots, or superseded notes.
4. **UNTESTED / UNKNOWN** — claims that have not been verified.

Do not silently convert historical or untested information into current fact.

## Core rules

- Inspect the actual repository and relevant files before modifying implementation.
- Preserve existing architecture unless the task explicitly requires changing it.
- Prefer small, surgical changes over scaffolding or duplicate systems.
- Do not create disposable helper files in project/home directories.
- For EcoFlow work, temporary scripts belong in `/tmp/`; permanent action scripts remain in the established energy skill structure.
- Do not paste large source files into chat when a path, diff, or concise summary is sufficient.
- Avoid creating duplicate copies of authoritative documents.
- When a durable architectural decision changes, update the applicable master-prompt documentation.
- When handing work to another agent, identify what is verified, what changed, and what remains unknown.

## Repository map

### US Mainland Server
`rootrecordsoftwaresolutions/US-Mainland-Server`

Use its own README, project documentation, skills, and source as authoritative for implementation details within that repository.

### Solar Pacific RootRecord Server
`rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server`

This repository contains major RootRecord server areas including agents, automations, energy, handoff, reports, state, and status. Use the repository's current contents rather than historical snapshots.

### RootRecord Website
`rootrecordsoftwaresolutions/RootRecord-Website`

Use its current repository documentation and source as authoritative for website implementation.

## Prompt selection

Read only the prompt files needed for the current task. `manifest/prompts.yaml` defines which prompts exist and whether they are required.

## Change discipline

Before changing a file:

1. Locate the actual current file.
2. Read enough surrounding context to understand its role.
3. Check for existing conventions.
4. Make the smallest change that satisfies the request.
5. Verify the result.
6. Report changed paths and verification evidence.

## Handoff discipline

A handoff should contain:

- current verified state;
- changes made;
- files/paths affected;
- tests or verification performed;
- unresolved questions;
- known historical information that should not be mistaken for current state.

Do not create a handoff merely to repeat information already present in the master-prompt repository.

## Updating this system

The master-prompt repository itself is version-controlled. Changes should be reviewed as normal repository changes. The generated ZIP is an output artifact, not a second source of truth.
