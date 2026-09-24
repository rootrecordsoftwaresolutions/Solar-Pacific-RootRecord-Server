# RootRecord Master Prompt

This repository is the durable cross-project operating context for RootRecord development and operations.

It is **not** a copy of the application repositories. It is the place to keep the rules, workflow conventions, repository map, frequently touched file links, and durable cross-project context that agents repeatedly need.

## Repositories

- Solar Pacific RootRecord Server: https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server
- US Mainland Server: https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server
- RootRecord Website: https://github.com/rootrecordsoftwaresolutions/RootRecord-Website
- RootRecord Master Prompt: https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt

## How to use this repository

Start with:

1. `MASTER-PROMPT.md`
2. `prompts/00-core.md`
3. `prompts/03-development.md` or `prompts/04-operations.md`
4. `prompts/05-energy.md` when energy/EcoFlow work is involved
5. `prompts/06-handoff.md`
6. `prompts/08-repository-and-file-links.md` when navigating code

`manifest/prompts.yaml` is the prompt inventory.

## Important distinction

This repository records **how RootRecord work should be done** and where important implementation files live.

The actual implementation remains in the project repositories. When a linked file moves, update this index rather than copying the implementation into this repository.

## Current workflow philosophy

The preferred loop is:

**inspect → patch → validate → independently double-check → hand off**

The agent should work efficiently, reuse the existing architecture, and avoid making the operator discover preventable mistakes.

## Evidence labels

Use these consistently:

- **Confirmed** — directly verified in the current source/live result.
- **Hypothesis** — plausible interpretation that still needs verification.
- **Unknown** — not established.
- **Historical** — preserved for context but not treated as current state.

## No silent reconciliation

When old handoff material conflicts with current implementation, do not silently rewrite history. Identify the conflict, inspect the current source, and record the resulting current state separately.
