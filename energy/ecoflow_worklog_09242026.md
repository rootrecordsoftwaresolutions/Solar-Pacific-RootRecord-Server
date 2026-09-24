# EcoFlow Worklog — RootRecord Data Layer Upgrade

**Project:** Solar-Pacific-RootRecord-Server
**Repository:** `rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server`
**Local repository root:** `/home/rootrecord/.ollama/skills`
**Primary plan:** `energy/ROOTRECORD-DATA-LAYER-UPGRADE-PLAN.md`
**Purpose:** Persistent working record of EcoFlow/source-data investigation and implementation decisions.

---

## 0. Worklog Purpose

This document exists beside the primary data-layer upgrade plan so future work can resume from the actual state discovered during investigation rather than relying on conversational memory.

This is a **working record**, not a replacement for the main architecture plan.

The main plan defines the intended nine-layer data architecture and implementation sequence.

This worklog records:

* what was actually inspected;
* what the current system actually does;
* what historical data actually contains;
* decisions made during the investigation;
* corrections to earlier assumptions;
* current device inventory;
* current code/data paths;
* constraints that must not be violated;
* unresolved questions;
* the exact next investigation step.

---

# 1. Critical Decisions / Corrections

## 1.1 Canonical EcoFlow database location

**DECISION:**

EcoFlow SQLite databases belong inside:

```text
/home/rootrecord/.ollama/skills/energy/data/
```

Do **not** use:

```text
/home/rootrecord/Database/ROOTRECORD/rootrecord.db
```

The latter appeared in an earlier version of the architecture plan as a generic canonical SQLite location, but it is **not the chosen location for the EcoFlow databases**.

The `energy/data/` directory is the intended canonical location for EcoFlow DB files.

The existing filesystem storage under:

```text
/home/rootrecord/Database/ENERGY/
```

is legacy/current production storage and is a migration boundary. It must not be silently moved, deleted, or rewritten during the audit.

---

## 1.2 Historical data is NOT being imported

Historical EcoFlow databases are being inspected **only to learn from their structure and real payloads**.

There is currently no requirement to import or migrate their historical records into the new database.

Historical databases therefore serve as:

* schema reference;
* payload reference;
* cadence/reference-quality evidence;
* compatibility information;
* migration-design evidence.

They are **not** the source for populating the new database.

---

## 1.3 Current EcoFlow inventory is THREE devices

An earlier historical database contained only two devices. That must **not** be interpreted as the current inventory.

Current device inventory from the master environment configuration:

| Logical device    | Serial number      | Name |
| ----------------- | ------------------ | ---- |
| Delta 2           | `R331ZAB5SG6S2858` | B2   |
| Delta 2 Secondary | `R331ZAB5SG755642` | B3   |
| River 2 Pro       | `R621ZA16XH6K1155` | B1   |

The current repository configuration only has active sections for the first Delta 2 and the River 2 Pro.

Therefore:

**There is currently a configuration/inventory gap for the second Delta 2 (`R331ZAB5SG755642`).**

This must be resolved deliberately during implementation rather than accidentally ignored.

---

# 2. Current Repository / Runtime Boundary

Local repository:

```text
/home/rootrecord/.ollama/skills
```

Energy skill:

```text
/home/rootrecord/.ollama/skills/energy
```

Current repository architecture includes:

```text
energy/
├── config/
├── data/
├── lib/
├── scripts/
└── ...
```

`energy/data/` currently exists and is intended to become the canonical location for EcoFlow SQLite databases.

At the time of audit, it was empty.

---

# 3. Current Production Data Path

The existing EcoFlow implementation still uses:

```text
/home/rootrecord/Database/ENERGY
```

with subdirectories including:

```text
samples/
ports/
soc/
watts/
```

The current configuration explicitly points there:

```ini
[paths]
energy_data=/home/rootrecord/Database/ENERGY
samples=/home/rootrecord/Database/ENERGY/samples
ports=/home/rootrecord/Database/ENERGY/ports
soc=/home/rootrecord/Database/ENERGY/soc
watts=/home/rootrecord/Database/ENERGY/watts
```

This is **current implementation**, not the desired final storage architecture.

Do not change these paths merely because the new architecture intends to replace them.

The migration plan explicitly requires source-data/schema work before producer changes.

---

# 4. Current BLE Ownership

Current BLE service:

```text
ava-ecoflow-ble.service
```

Current owner script:

```text
/home/rootrecord/.ollama/skills/energy/scripts/ble/ble-owner.py
```

The owner is intentionally thin.

Its current purpose is essentially:

* claim/maintain ownership;
* provide a heartbeat;
* avoid aggressive polling;
* leave actual short BLE sessions to atomic actions.

The service currently uses:

```text
ENERGY_BLE_OWNER_INTERVAL_S=30
```

The owner itself is **not currently the telemetry polling engine**.

Do not create a second BLE owner or competing polling system.

---

# 5. Current Measurement Producer

The current measurement producer is:

```text
energy/lib/read_runner.py
```

Its basic flow is:

```text
read_runner
    ↓
ble_client.connect(alias)
    ↓
eflib device implementation
    ↓
read device properties
    ↓
construct snapshot
    ↓
write JSON compatibility/output files
```

The current reader extracts fields including:

```text
ac_ports
usb_ports
dc_12v_port

ac_output_power
ac_input_power

usbc_output_power
usba_output_power

xt60_input_power
solar_input_power (fallback)

battery_level
soc (fallback)
```

The current implementation writes measurement artifacts to the legacy filesystem locations.

It does **not** yet write the proposed canonical SQLite data layer.

---

# 6. Current BLE Client

Current BLE client:

```text
energy/lib/ble_client.py
```

It:

1. loads the master environment;
2. obtains the EcoFlow user/account ID;
3. loads device configuration;
4. selects the device serial number;
5. selects the eflib module;
6. scans for the configured BLE MAC;
7. instantiates the appropriate `eflib` `Device`;
8. connects/authenticates;
9. permits the caller to read or operate on the device.

Current device module selection comes from `devices.conf`.

The BLE client is therefore the existing integration boundary that should be preserved during the migration.

---

# 7. Current Configuration

Current:

```text
energy/config/devices.conf
```

contains:

```ini
[delta2]
model=Delta 2
alias=delta2
sn=R331ZAB5SG6S2858
mac=24:58:7C:20:92:61
role=unassigned
eflib_module=eflib.devices.delta2

[river2pro]
model=River 2 Pro
alias=river2pro
sn=R621ZA16XH6K1155
mac=DC:06:75:56:AC:1D
role=laptop_ac_car_dc
eflib_module=eflib.devices.river2_pro
```

There is currently **no `[delta2_secondary]` / equivalent section** for:

```text
R331ZAB5SG755642
```

The master environment nevertheless identifies that device.

This discrepancy is an important implementation item.

---

# 8. Master Environment Device Inventory

The master environment is:

```text
/home/rootrecord/master/master-key.env
```

Relevant device inventory entries are:

```text
ECOFLOW_DELTA_2=R331ZAB5SG6S2858
ECOFLOW_DELTA_2_SECONDARY=R331ZAB5SG755642
ECOFLOW_RIVER_2_PRO=R621ZA16XH6K1155
```

Names:

```text
ECOFLOW_DELTA_2_NAME=B2
ECOFLOW_DELTA_2_SECONDARY_NAME=B3
ECOFLOW_RIVER_2_PRO_NAME=B1
```

The environment file is secret-bearing infrastructure.

**Never copy its secrets into GitHub or this worklog.**

Only non-secret inventory information should be documented.

---

# 9. Current EFLIB Findings

The current bundled EcoFlow library was inspected directly.

## 9.1 Delta 2 implementation

File:

```text
energy/lib/vendor/eflib/devices/delta2.py
```

The Delta 2 class derives from:

```text
Delta2Base
```

and exposes, among other fields:

```text
ac_input_power
energy_backup
energy_backup_battery_level
dc_output_power
ac_charging_speed
ac_charging
disable_grid_bypass
xt60_input_power
```

The class also implements control operations such as:

```text
enable_energy_backup
set_energy_backup_battery_level
set_ac_charging_speed
enable_ac_charging
enable_disable_grid_bypass
```

This confirms that the device object is considerably richer than the small subset currently collected by `read_runner.py`.

---

# 10. Delta 2 Base Measurement Surface

File:

```text
energy/lib/vendor/eflib/devices/_delta2_base.py
```

The Delta 2 base exposes significantly more telemetry than the current reader consumes.

Important fields identified include:

## AC

```text
ac_output_power
ac_input_voltage
ac_input_current
ac_output_voltage
ac_output_current
```

## Battery

```text
battery_level_main
battery_1_enabled
battery_1_battery_level
battery_1_cell_temperature
battery_1_voltage
battery_1_max_cell_voltage
battery_1_min_cell_voltage
battery_1_sn

battery_2_enabled
battery_2_battery_level
battery_2_cell_temperature
battery_2_voltage
battery_2_max_cell_voltage
battery_2_min_cell_voltage
battery_2_sn

battery_level
```

## Aggregate power

```text
input_power
output_power
```

## USB

```text
usbc_output_power
usbc2_output_power
usba_output_power
usba2_output_power
qc_usb1_output_power
qc_usb2_output_power
```

## Port states

```text
ac_ports
usb_ports
dc_12v_port
```

## Battery limits / time estimates

```text
battery_charge_limit_min
battery_charge_limit_max
remaining_time_charging
remaining_time_discharging
```

## Battery electrical measurements

```text
cell_temperature
battery_voltage
max_cell_voltage
min_cell_voltage
```

## DC / solar-side electrical measurements

```text
dc_input_voltage
dc_input_current
```

## 12V output electrical measurements

```text
dc12v_output_voltage
dc12v_output_current
```

This is important for schema design.

The future SQLite schema should be designed against the **actual available measurement surface**, rather than preserving only the old small JSON subset.

However, availability does not mean every field must necessarily be sampled into every resolution layer.

---

# 11. Delta 2 Extra-Battery Discovery

The Delta 2 implementation also contains explicit handling for additional batteries.

It can identify up to two extra battery slots in this model implementation:

```text
battery_1_*
battery_2_*
```

The implementation can expose:

```text
battery_1_enabled
battery_1_sn
battery_1_battery_level

battery_2_enabled
battery_2_sn
battery_2_battery_level
```

The vendor mapping layer supports a generalized extra-battery model with up to:

```text
MAX_EXTRA_BATTERIES = 10
```

This is relevant to the future schema.

Do not hard-code the assumption that every EcoFlow device has exactly one battery entity.

---

# 12. River 2 Pro Implementation

File:

```text
energy/lib/vendor/eflib/devices/river2_pro.py
```

The River 2 Pro implementation derives from:

```text
river2.Device
```

and identifies the River 2 Pro serial prefixes:

```text
R621
R623
```

The current configured device:

```text
R621ZA16XH6K1155
```

therefore matches the supported River 2 Pro implementation.

Further River 2/River 2 Pro field inventory should be inspected before final schema lock.

---

# 13. Device Base Findings

File:

```text
energy/lib/vendor/eflib/devicebase.py
```

The base device model confirms that the eflib device object is stateful and event-driven.

Important observations:

* properties are updated from incoming BLE packets;
* device fields can have missing/default behavior;
* device connections have explicit authenticated states;
* device properties can trigger callbacks;
* packet parsing updates model fields;
* connection state and diagnostics exist separately from measurements.

The library also has a missing-field grace mechanism:

```text
MISSING_DEFAULT_GRACE = 10
```

and supports `default_when_missing(...)`.

This matters for the new data layer:

**A missing field must not automatically be interpreted as a measured zero.**

The architecture plan already establishes:

> never fabricate missing data.

That rule applies here.

A field that is unavailable because its corresponding packet did not arrive must remain distinguishable from a genuine measured zero.

---

# 14. Units Currently Defined

File:

```text
energy/lib/vendor/eflib/entity/units.py
```

Currently defined units include:

```text
Power      W
Temperature C / F
Current    A
Voltage    V
```

Battery percentage fields and time-duration fields are represented through the property system but are not defined as explicit units in this file.

The future database schema should establish its own explicit unit semantics rather than relying solely on Python property names.

---

# 15. Device Mapping Findings

File:

```text
energy/lib/vendor/eflib/device_mappings.py
```

The library maintains a broad EcoFlow model/serial-prefix mapping.

Relevant mappings include:

```text
R331 → EcoFlow DELTA 2
R335 → EcoFlow DELTA 2

R621 → EcoFlow RIVER 2 Pro
R623 → EcoFlow RIVER 2 Pro
```

This confirms the current device classifications from the serial numbers.

The mapping also distinguishes packet generations (`v1`, `v2`, `v3`, etc.).

Current devices are:

```text
Delta 2 → v2 family
River 2 Pro → v2 family
```

---

# 16. Historical EcoFlow Database Findings

Historical databases were inspected read-only.

They were found under the older EcoFlow storage area:

```text
/home/rootrecord/.ollama/old skills/energy/ecoflow-ble-poller/store/
```

Relevant files included:

```text
ecoflow-10s.db
ecoflow-1min.db
ecoflow-state.db
```

These are **historical reference material only**.

---

# 17. Historical `ecoflow-10s.db`

The historical high-resolution DB contained:

```text
devices
snapshots
sqlite_sequence
```

The `snapshots` table included fields:

```text
id
ts
sn
online
soc
in_w
out_w
solar_w
raw_json
created_at
```

There was an index on:

```text
(sn, ts)
```

The historical DB contained approximately:

```text
16,487 snapshot rows
```

and represented two devices.

This two-device historical state is **not the current three-device inventory**.

---

# 18. Historical Raw Payload

Historical raw JSON examples included fields equivalent to:

```json
{
  "at": "...",
  "deviceOnline": true,
  "soc": 35.0,
  "solarW": 32.0,
  "inW": 0,
  "outW": 29.0,
  "offCircuit": false
}
```

Some historical rows additionally contained:

```text
sn
source
```

The historical data therefore confirms a simple core telemetry vocabulary:

```text
timestamp
device identity
online state
SOC
input watts
output watts
solar watts
```

but the current eflib inspection shows that the actual available measurement surface is much richer.

The new schema should therefore not be constrained to the historical minimal payload.

---

# 19. Historical Cadence Finding

The historical database was called/treated as a `10s` layer, but inspection showed that actual timestamp spacing was **not a fixed 10-second cadence**.

Observed timestamp gaps included:

* very small gaps;
* gaps around normal polling intervals;
* very large gaps.

The largest observed gap was roughly:

```text
32,500 seconds
```

Therefore:

**Layer names must describe intended resolution/aggregation, not imply that every row is guaranteed to exist at that exact cadence.**

Missing observations must remain missing.

This reinforces the main architecture rule:

> Never fabricate missing data.

---

# 20. Historical Value Ranges

Historical inspected ranges included approximately:

```text
SOC:      0–100
input W:  0–963
output W: 0–226
solar W:  0–450
```

The historical averages were approximately:

```text
SOC       24.9
input W   55.7
output W  49.0
solar W   49.2
```

These values are descriptive of the historical sample and should **not** be treated as current operating values.

---

# 21. Historical Summary Schema

An older summary database contained a much broader aggregation schema.

Fields included:

```text
id
ts
bucket_key
level
sn
name
samples
source_rows

soc_avg
soc_min
soc_max
soc_delta
soc_stdev

in_w_avg
in_w_min
in_w_max
in_w_delta

out_w_avg
out_w_min
out_w_max
out_w_delta

solar_w_avg
solar_w_min
solar_w_max

net_w_avg
load_ratio

energy_in_wh
energy_out_wh
energy_solar_wh

online_pct
trend
meta_json
created_at
```

The historical summary table itself had no populated rows when inspected.

This schema is useful as evidence of fields previously considered useful, but it is **not automatically the final schema**.

The new schema must be derived from:

1. the current architecture plan;
2. actual current eflib properties;
3. actual current device inventory;
4. actual producer behavior;
5. the required nine-layer condensation model.

---

# 22. Historical State DB

The historical state DB contained a watermark structure equivalent to:

```text
watermark(
    level,
    last_id,
    last_ts,
    updated_at
)
```

It contained no populated watermark rows at inspection time.

This is useful architectural evidence for persisted condensation state.

However, the final implementation should make condensation idempotent and self-healing from persisted source data rather than depending solely on scheduler memory.

---

# 23. Nine-Layer Architecture

The main plan defines nine layers:

```text
1sec
1min
5min
15min
1hour
day
7days
month
year
```

The intended model is:

### Working/resetting layers

```text
1sec
1min
5min
15min
1hour
```

### Permanent historical layers

```text
day
7days
month
year
```

The exact implementation details remain governed by:

```text
energy/ROOTRECORD-DATA-LAYER-UPGRADE-PLAN.md
```

---

# 24. Condensation Rules

The planned condensation model is:

```text
1sec → 1min
1min → longer aggregation layers
5min → day
15min → day
1hour → day
day → 7days
7days → month
month → year
```

Important boundary behavior:

* `1sec` is condensed into `1min`;
* verified source data can then be cleared from the resetting layer;
* daily aggregation occurs at the 24-hour boundary;
* weekly aggregation occurs at the Sunday boundary;
* monthly/yearly boundaries follow wall-clock calendar boundaries;
* missed boundaries must self-heal after restart;
* condensation must be idempotent;
* lower-resolution source data must not be discarded until the upper layer is verified.

---

# 25. Scheduler Constraint

The existing system already has scheduling/polling infrastructure.

Do **not** introduce a competing scheduler.

The eventual condensation scheduler should integrate with the existing scheduler/poller architecture.

A previous audit identified an important constraint:

A single-threaded scheduler can miss an `ON_AT` boundary if a long BLE action blocks it.

Therefore the final scheduler must be:

* wall-clock based;
* persisted/self-healing;
* capable of recognizing missed boundaries;
* not dependent solely on process uptime or in-memory timers.

---

# 26. GitHub Storage Boundary

GitHub is for:

```text
code
configuration
schemas
documentation
skills
```

GitHub must **not** receive:

```text
telemetry
logs
SQLite databases
disposable runtime state
```

The EcoFlow DBs therefore belong under:

```text
energy/data/
```

locally/runtime-side, with appropriate Git exclusion.

The existing Git synchronization machinery should be preserved.

---

# 27. Git Synchronization Constraint

The existing Git push workflow already includes conflict-aware behavior.

The current architecture includes scripts such as:

```text
github/scripts/push-repo-once.sh
github/scripts/poll-and-push.sh
github/scripts/sync-all.sh
```

The existing sync behavior is intended to:

```text
local changes
→ commit
→ fetch
→ compare
→ merge if necessary
→ push
```

with safe handling of conflicts.

Do not replace this with a second sync pipeline.

Do not introduce telemetry/database uploads into Git sync.

---

# 28. Current Git Working Tree Caution

During the audit, a live log file was modified:

```text
logs/store/ava-ecoflow-ble.log
```

This must not be casually discarded.

Any future cleanup must distinguish:

* intentional code/config changes;
* runtime log changes;
* generated runtime artifacts;
* tracked/untracked telemetry.

---

# 29. Migration Principles

The migration must be staged.

Current intended order:

```text
1. Audit
2. Source data inventory
3. Finalize schema against real payloads
4. Build DB skill
5. Initialize empty DB
6. BLE → DB migration
7. Dual-write validation
8. Full BLE cutover
9. Git runtime cleanup
10. Condensation engine
11. Wall-clock scheduler integration
12. Exact-boundary Git sync
13. JSON reduction
14. Read-only LLM DB interface
15. Thin Mainland/AWS edge
16. Failure/rollback tests
17. Production cutover
```

Do not skip directly to database initialization.

---

# 30. Explicit Audit Constraints

Until the architecture is finalized:

**Do not:**

* delete existing data;
* migrate historical data;
* move existing production storage;
* initialize a DB over existing data;
* replace the BLE ingestion architecture;
* replace the scheduler;
* create a second competing poller;
* create a second competing Git sync;
* enable disabled aggressive polling;
* modify production/Mainland deployment;
* change Git remotes;
* change branches;
* use destructive Git commands;
* fabricate missing measurements;
* silently convert missing measurements to zero.

---

# 31. Current Known Configuration Gap

There are currently three EcoFlow devices known from the master environment:

```text
B1 → R621ZA16XH6K1155 → River 2 Pro
B2 → R331ZAB5SG6S2858 → Delta 2
B3 → R331ZAB5SG755642 → Delta 2
```

but only two device sections currently exist in:

```text
energy/config/devices.conf
```

Therefore, before any final production migration, we need to establish:

1. the BLE MAC for B3;
2. the desired alias;
3. the desired role;
4. the correct configuration representation;
5. whether the existing BLE client requires any special handling for multiple Delta 2 devices.

Do not invent the MAC address.

---

# 32. Current Schema Design Direction

The new database schema should distinguish at minimum between:

## Device identity

```text
device
serial number
model
alias/name
role
```

## Observation identity

```text
timestamp
source
online/connectivity state
```

## Electrical measurements

```text
power
voltage
current
```

## Battery measurements

```text
SOC
battery voltage
cell voltage
cell temperature
charge/discharge limits
remaining charge/discharge time
```

## Port state

```text
AC
USB
12V/DC
```

## Solar/DC input

```text
solar/DC input power
DC voltage
DC current
```

## Multi-battery topology

```text
battery slot
battery serial
enabled state
battery SOC
battery electrical/temperature measurements
```

The final normalized schema remains to be designed.

---

# 33. Important Measurement Semantics

The eflib inspection establishes that there are multiple potentially overlapping power properties.

Examples:

```text
ac_input_power
input_power

ac_output_power
output_power

xt60_input_power
dc_output_power
```

These should **not** be casually collapsed into a single generic watt value without preserving their semantic meaning.

The schema must distinguish measurement channels sufficiently to answer questions such as:

* AC input versus total input;
* AC output versus total output;
* solar/DC input;
* USB output;
* 12V output;
* other device-specific DC paths.

This is a schema-design issue, not a naming cleanup issue.

---

# 34. Missing vs Zero

This is a hard requirement.

Example:

```text
0 W
```

can mean:

> the device actually reported zero watts.

Whereas:

```text
NULL / missing
```

can mean:

> the relevant packet/field was unavailable.

These are not interchangeable.

The existing eflib library itself has explicit missing-field/default behavior, which reinforces the need for this distinction.

---

# 35. Current State: What Has NOT Happened

At the point this worklog was created:

* no new EcoFlow SQLite DB has been initialized;
* no historical data has been imported;
* no historical data has been migrated;
* no production BLE producer has been cut over;
* no new polling buckets have been enabled;
* no existing scheduler has been replaced;
* no existing Git sync has been replaced;
* no production deployment has been altered;
* no existing `Database/ENERGY` data has been moved.

The investigation remains in the **audit/source-inventory/schema-definition stage**.

---

# 36. Immediate Next Investigation

The next task is to inspect the River 2 implementation and remaining relevant eflib property definitions sufficiently to complete the real measurement inventory.

The last command executed inspected:

```text
delta2.py
_delta2_base.py
river2_pro.py
devicebase.py
device_mappings.py
entity/units.py
devices.conf
```

The next work should build on this output rather than repeating the same inspection.

Particular goal:

**Determine the complete practical telemetry surface currently available for the three current device identities, while distinguishing common fields from device-specific fields.**

Do not modify code during this step.

---

# 37. Working Terminology

Use these terms consistently:

### Device

A physical EcoFlow unit identified by serial number.

### Measurement

A value actually obtained from the device.

### Observation

A timestamped collection of measurements from a device.

### Source

The mechanism that produced the observation, currently BLE.

### Working layer

A resolution that may be reset/condensed after verified aggregation.

### Historical layer

A permanent aggregate retained as historical record.

### Condensation

The verified transformation of lower-resolution observations into a higher-resolution aggregate.

### Missing

No valid measurement was obtained.

### Zero

The device actually reported zero.

---

# 38. Resume Point

When continuing work from this document:

1. Read this worklog.
2. Read `energy/ROOTRECORD-DATA-LAYER-UPGRADE-PLAN.md`.
3. Treat `energy/data/` as the chosen EcoFlow DB location.
4. Treat the three-device inventory as authoritative for the current system:

   * B1 / River 2 Pro
   * B2 / Delta 2
   * B3 / Delta 2 Secondary
5. Treat historical DBs as reference only.
6. Do not import historical data.
7. Do not assume the two-device historical inventory is current.
8. Do not modify production paths or pollers during schema investigation.
9. Finish the real current telemetry/property inventory before locking the SQLite schema.
10. Preserve the existing BLE owner and existing synchronization architecture.
11. Never fabricate missing values.
12. Never confuse legacy `Database/ENERGY` storage with the intended new canonical `energy/data/` SQLite location.

---

# 39. Source Evidence Used for This Worklog

This worklog was assembled from the actual RootRecord investigation outputs and repository/code inspection performed during this project.

Key inspected sources included:

```text
energy/config/devices.conf

energy/lib/ble_client.py
energy/lib/config.py
energy/lib/envload.py
energy/lib/paths.py
energy/lib/read_runner.py
energy/lib/action_runner.py

energy/scripts/ble/ble-owner.py

energy/lib/vendor/eflib/devices/delta2.py
energy/lib/vendor/eflib/devices/_delta2_base.py
energy/lib/vendor/eflib/devices/river2_pro.py
energy/lib/vendor/eflib/devicebase.py
energy/lib/vendor/eflib/device_mappings.py
energy/lib/vendor/eflib/entity/units.py
```

Historical reference databases inspected included:

```text
/home/rootrecord/.ollama/old skills/energy/ecoflow-ble-poller/store/ecoflow-10s.db
/home/rootrecord/.ollama/old skills/energy/ecoflow-ble-poller/store/ecoflow-1min.db
/home/rootrecord/.ollama/old skills/energy/ecoflow-ble-poller/store/ecoflow-state.db
```

The primary architecture plan remains:

```text
energy/ROOTRECORD-DATA-LAYER-UPGRADE-PLAN.md
```

---

# 40. Final Status

**STATUS: AUDIT / SOURCE INVENTORY IN PROGRESS**

No implementation cutover has occurred.

The major architectural decisions currently established are:

```text
EcoFlow DB location:
    /home/rootrecord/.ollama/skills/energy/data/

Historical data:
    inspect only; do not import

Current devices:
    B1 = River 2 Pro
    B2 = Delta 2
    B3 = Delta 2 Secondary

Existing BLE owner:
    preserve

Existing producer:
    preserve until migration stage

Existing Git sync:
    preserve

Existing Database/ENERGY:
    legacy/current migration boundary

New architecture:
    SQLite-first
    nine resolution layers
    wall-clock boundaries
    persisted/self-healing condensation
    no fabricated measurements

Current next step:
    complete telemetry/property inventory before finalizing schema
```

**Do not treat this document as evidence that any of the future migration stages have already been implemented.**

