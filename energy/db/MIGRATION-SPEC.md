# RootRecord SQLite Data Layer — Migration Specification

## Target

Canonical database:

`/home/rootrecord/Database/ROOTRECORD/rootrecord.db`

This specification builds the database layer only. It does not initialize or migrate production data by itself.

## Model

- `device`: top-level monitored EcoFlow units.
- `battery`: primary battery plus zero or more expansion batteries.
- `device_port`: discovered physical/logical ports.
- `observation`: immutable timestamped telemetry envelope.
- Measurement tables preserve per-field state:
  - `measured`
  - `defaulted` — only where EFLIB explicitly supplies a default for a missing packet.
  - `missing`
  - `not_applicable`
- B3 is represented as an expansion `battery` belonging to B2; it is not a third top-level `device`.
- Raw source payloads remain attached to observations for forensic/replay use.

## Metric domains

### Device measurements

Examples:

- `battery_level`
- `input_power`
- `output_power`
- `remaining_time_charging`
- `remaining_time_discharging`
- `battery_charge_limit_min`
- `battery_charge_limit_max`
- `energy_backup`
- `energy_backup_battery_level`
- `dc_mode`
- charging configuration/state

### Battery measurements

Examples:

- `soc_percent`
- `voltage_v`
- `cell_voltage_max_v`
- `cell_voltage_min_v`
- `temperature_c`
- `charge_limit_min_pct`
- `charge_limit_max_pct`
- `remaining_charge_s`
- `remaining_discharge_s`

### Electrical measurements

Channels are dynamic and device-specific. Known channels include:

`input_total`, `output_total`, `ac_input`, `ac_output`, `dc_input`, `dc_output`, `solar_input`, `car_input`, `usb_c_1`, `usb_c_2`, `usb_a_1`, `usb_a_2`, `qc_usb_1`, `qc_usb_2`, `dc12v_output`.

### Port measurements

Ports are discovered into `device_port`; telemetry is attached to those identities rather than assuming a fixed port count.

## Timestamp rule

Store observation timestamps as UTC ISO-8601 text with an explicit `Z` suffix. Wall-clock/local-time conversion belongs to the condensation scheduler, not the canonical observation timestamp.

## Idempotency

The observation uniqueness key is:

`device_id + observed_at + source_id + source_sequence`

Measurement rows are unique within their observation and subject.

Aggregation is unique by:

`layer + period_start + period_end`

and therefore safe to retry.

## Migration sequence

1. Create the empty schema.
2. Register source/parser metadata.
3. Discover/create top-level devices.
4. Discover/create primary and expansion batteries.
5. Discover/create ports.
6. Import observations in chronological order.
7. Import structured measurements without converting missing values to zero.
8. Attach raw payloads where available.
9. Verify counts, timestamp ranges, device relationships, and state semantics.
10. Only after verification, enable the producer's SQLite write path.
11. Preserve original JSON/log sources until the migration is independently verified.

## Aggregation rules

Layers are exactly:

`1sec → 1min → 5min → 15min → 1hour → day → 7days → month → year`

- Working layers may be condensed/reset only after the destination run is complete and verified.
- Permanent layers are append-only.
- Missing samples do not become zero.
- Energy calculations use actual elapsed observation intervals and coverage.
- Aggregation must be restart-safe and idempotent.
- A missed boundary is recovered from persisted timestamps on the next run.

## Explicit non-goals

- No production database initialization.
- No JSON deletion.
- No log deletion/truncation.
- No scheduler replacement.
- No second BLE pipeline.
- No GitHub telemetry storage.
