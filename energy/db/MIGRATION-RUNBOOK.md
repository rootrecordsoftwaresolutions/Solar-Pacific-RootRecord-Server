# Legacy JSON → SQLite Migration

The migration is additive and reversible. Legacy JSON remains untouched until an explicit operator retirement decision.

## Import
Use energy/scripts/migrate_json.py with an explicit source file, device serial, and model.

Each source file receives its own legacy_json observation source. Timestamps are normalized to UTC Z. Scalar JSON fields become typed device measurements; null remains missing.

## Verification
Before retiring any legacy writer:
1. Count source records.
2. Count imported observations.
3. Compare earliest/latest timestamps.
4. Compare representative SOC and power values.
5. Run condensation layers over the imported range.
6. Confirm no source files were modified.

The migration does not delete, rewrite, or rename legacy files.
