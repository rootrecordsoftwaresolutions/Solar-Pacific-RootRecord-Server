# RootRecord Data Layer — Operational Path

The live reader persists normalized EcoFlow telemetry into SQLite before the legacy JSON compatibility outputs are written.

## Runtime flow

EcoFlow BLE -> EFLIB parser -> read_runner -> SQLite observation + typed measurements -> condensation engine -> legacy JSON compatibility output.

## Condensation

Supported layers:

1sec, 1min, 5min, 15min, 1hour, day, 7days, month, year.

Aggregation is additive and restart-safe. Missing observations are never converted to zero. Power energy is calculated from elapsed valid measurement intervals.

## Verification

Run the explicit verifier against the target database before retiring legacy storage:

python3 energy/scripts/verify_rootrecord_db.py

No destructive migration is performed by the verifier.
