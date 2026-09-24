---
name: dev-prompts
description: Load and apply the RootRecord Master Prompt and the applicable prompt files before development or operational work.
---

# RootRecord Dev Prompts Skill

## Purpose

Use the RootRecord Master Prompt as the cross-project operating contract.

## Canonical source

The authoritative master-prompt repository is:

`https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt`

## Procedure

1. Load `MASTER-PROMPT.md`.
2. Load the prompt files applicable to the current task.
3. Inspect the actual target repository before changing anything.
4. Classify important facts as LIVE VERIFIED, DOCUMENTED POLICY, HISTORICAL, or UNTESTED / UNKNOWN.
5. Make the smallest appropriate change.
6. Verify the result.
7. Report changed paths and evidence.

## Temporary files

For RootRecord work, do not leave disposable helper scripts in project/home directories. Use `/tmp/` when temporary files are actually needed.

## Durable changes

If a durable architectural or workflow decision changes, update the appropriate master-prompt file rather than creating an isolated copy in another repository.
