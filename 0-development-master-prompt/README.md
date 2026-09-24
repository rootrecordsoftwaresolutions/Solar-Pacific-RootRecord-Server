# RootRecord Master Prompt

Central source of truth for how RootRecord agents should understand and work across the RootRecord repositories.

## Repositories

- `rootrecordsoftwaresolutions/US-Mainland-Server`
- `rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server`
- `rootrecordsoftwaresolutions/RootRecord-Website`

## Design principles

1. Keep this repository authoritative for durable cross-project operating rules.
2. Do not duplicate application source code here.
3. Prefer repository-native documentation for implementation details.
4. Distinguish verified live state from documented policy, historical information, and unknown/untested claims.
5. Keep temporary work out of project directories; for EcoFlow work, use `/tmp/` for disposable helpers.
6. Permanent EcoFlow action scripts belong under the existing energy skill's intended scripts directory.
7. Changes to durable architecture or workflow should be reflected in the appropriate prompt file.

## Loading

Start with `MASTER-PROMPT.md`, then consult the prompt files applicable to the task. The manifest in `manifest/prompts.yaml` is the authoritative inventory.
