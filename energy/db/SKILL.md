# RootRecord SQLite Data Layer

This directory contains the canonical SQLite schema and persistence primitives for
the Energy/EcoFlow data-layer upgrade.

## Files

- `schema.sql` — schema definition; safe to execute repeatedly.
- `store.py` — transactional persistence primitives; no automatic DB creation.
- `MIGRATION-SPEC.md` — migration and semantic rules.
- `../scripts/init_rootrecord_db.py` — explicit schema initializer.

## Important

The database is not initialized by importing this package.

The target production database is:

`/home/rootrecord/Database/ROOTRECORD/rootrecord.db`

Telemetry producers must explicitly call the persistence functions. The module
does not replace the existing BLE/poller path yet.

## State semantics

- `measured` — source supplied a real measurement, including measured zero.
- `defaulted` — EFLIB explicitly supplied a configured default because the
  source packet was absent.
- `missing` — source/packet did not provide a valid measurement.
- `not_applicable` — metric does not apply to this hardware.

Never encode missing or not-applicable as numeric zero.
