#!/usr/bin/env python3
"""Verify RootRecord SQLite integrity and aggregation readiness (split db layout)."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect, initialize_schema, connect_layer, DEFAULT_DB_PATH
from energy.db.aggregate import LAYERS


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path)
    args = p.parse_args()
    raw_path = args.db or DEFAULT_DB_PATH
    c = connect(raw_path)
    initialize_schema(c)
    checks = []
    for table in ("device", "battery", "device_port", "observation",
                  "device_measurement", "battery_measurement",
                  "electrical_measurement", "port_measurement"):
        n = c.execute("SELECT COUNT(*) FROM " + table).fetchone()[0]
        checks.append((table, n))
    fk = c.execute("PRAGMA foreign_key_check").fetchall()
    dup = c.execute("""SELECT device_id,observed_at,source_id,source_sequence,COUNT(*) n
                     FROM observation GROUP BY 1,2,3,4 HAVING n>1""").fetchall()
    bad_counts = {}
    for table in ("device_measurement", "battery_measurement", "port_measurement"):
        bad_counts[table] = c.execute("""SELECT COUNT(*) FROM """ + table + """
                         WHERE (state IN ('missing','not_applicable') AND (value_num IS NOT NULL OR value_text IS NOT NULL OR value_bool IS NOT NULL))
                            OR (state IN ('measured','defaulted') AND
                                ((value_num IS NOT NULL)+(value_text IS NOT NULL)+(value_bool IS NOT NULL))<>1)""").fetchone()[0]
    bad_electrical = c.execute("""SELECT COUNT(*) FROM electrical_measurement
                         WHERE (state IN ('missing','not_applicable') AND value_num IS NOT NULL)
                            OR (state IN ('measured','defaulted') AND value_num IS NULL)""").fetchone()[0]
    c.close()

    print("ROOTRECORD_DB_VERIFY")
    for t, n in checks:
        print(f"{t}={n}")
    print(f"foreign_key_errors={len(fk)}")
    print(f"duplicate_observations={len(dup)}")
    for table, n in bad_counts.items():
        print(f"invalid_{table}={n}")
    print(f"invalid_electrical_measurements={bad_electrical}")

    agg_ok = True
    for layer in LAYERS:
        lc = connect_layer(layer, raw_path)
        bad_aggregate = lc.execute("""SELECT COUNT(*) FROM aggregate_measurement
                             WHERE observed_span_s IS NOT NULL AND observed_span_s < 0
                                OR valid_duration_s IS NOT NULL AND valid_duration_s < 0
                                OR coverage_pct IS NOT NULL AND (coverage_pct < 0 OR coverage_pct > 100)
                                OR sample_count < 0 OR valid_sample_count < 0
                                OR valid_sample_count > sample_count""").fetchone()[0]
        bad_subjects = lc.execute("""SELECT COUNT(*) FROM aggregate_measurement am
                             LEFT JOIN raw.device d ON am.subject_type='device' AND d.device_id=am.subject_id
                             LEFT JOIN raw.battery b ON am.subject_type='battery' AND b.battery_id=am.subject_id
                             LEFT JOIN raw.device_port p ON am.subject_type='port' AND p.port_id=am.subject_id
                             WHERE (am.subject_type='device' AND d.device_id IS NULL)
                                OR (am.subject_type='battery' AND b.battery_id IS NULL)
                                OR (am.subject_type='port' AND p.port_id IS NULL)""").fetchone()[0]
        rows = lc.execute("SELECT COUNT(*) FROM aggregate_measurement").fetchone()[0]
        lc.close()
        print(f"layer={layer} aggregate_measurement_rows={rows} invalid_aggregate_rows={bad_aggregate} invalid_aggregate_subjects={bad_subjects}")
        if bad_aggregate or bad_subjects:
            agg_ok = False

    ok = not fk and not dup and not any(bad_counts.values()) and bad_electrical == 0 and agg_ok
    print("STATUS=" + ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
