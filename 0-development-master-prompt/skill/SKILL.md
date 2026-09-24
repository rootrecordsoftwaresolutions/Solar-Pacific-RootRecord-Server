---
name: dev-prompts
description: Load the RootRecord Master Prompt and the applicable prompt files before RootRecord development or operational work.
---

# RootRecord Dev Prompts Skill

## Canonical repository

https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt

## Procedure

1. Load `MASTER-PROMPT.md`.
2. Load the applicable prompt files.
3. Load `prompts/08-repository-and-file-links.md` when navigating or changing frequently touched files.
4. Inspect the actual target repository.
5. Classify material facts as Confirmed, Hypothesis, Unknown, or Historical.
6. Patch the existing final path.
7. Validate.
8. Independently double-check.
9. Hand off with exact paths and evidence.

## Existing-work rule

Do not create alternate roots, v2 trees, duplicate implementations, or migration scaffolding unless explicitly requested.

## Temporary work

Use `/tmp/` for disposable helpers.

Permanent EcoFlow action scripts remain in the existing energy skill structure.

## Operator workflow

When a manual command is required, follow the established one-paste-safe-block workflow and use absolute paths.
