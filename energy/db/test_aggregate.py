"""Focused regression tests for the RootRecord condensation engine."""
from __future__ import annotations

import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from energy.db.aggregate import aggregate_at
from energy.db.store import (
    add_device_measurement,
    add_port_measurement,
    connect,
    create_observation,
    initialize_schema,
    upsert_device,
)


class AggregateRegressionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.tmp.close()
        self.db = Path(self.tmp.name)
        self.conn = connect(self.db)
        initialize_schema(self.conn)
        self.device = upsert_device(
            self.conn,
            serial_number="TEST-SERIAL",
            model="Test Device",
            alias="test",
            observed_at="2026-09-24T22:00:00.000Z",
        )
        self.source = self.conn.execute(
            """INSERT INTO observation_source
               (source_type,source_name,parser_name,parser_version,created_at)
               VALUES ('test','aggregate-regression','unittest','1',
                       '2026-09-24T22:00:00.000Z')"""
        ).lastrowid

    def tearDown(self):
        self.conn.close()
        self.db.unlink(missing_ok=True)
        for suffix in ("-wal", "-shm"):
            Path(str(self.db) + suffix).unlink(missing_ok=True)

    def observation(self, stamp, power=None):
        obs = create_observation(
            self.conn,
            device_id=self.device,
            observed_at=stamp,
            source_id=self.source,
            online=True,
        )
        if power is not None:
            add_device_measurement(
                self.conn,
                observation_id=obs,
                metric_key="input_power",
                value=power,
                unit="W",
                state="measured",
            )
        return obs

    def test_power_crosses_period_boundary_without_losing_edge_energy(self):
        self.observation("2026-09-24T21:59:30.000Z", 100)
        self.observation("2026-09-24T22:00:30.000Z", 100)
        self.observation("2026-09-24T22:01:30.000Z", 100)
        self.conn.commit()

        aggregate_at(
            self.conn,
            "1min",
            datetime(2026, 9, 24, 22, 0, tzinfo=timezone.utc),
        )

        row = self.conn.execute(
            """SELECT sample_count,coverage_pct,energy_wh
               FROM aggregate_measurement am
               JOIN aggregation_run ar ON ar.aggregation_run_id=am.aggregation_run_id
               WHERE ar.layer='1min'
                 AND ar.period_start='2026-09-24T22:00:00.000Z'
                 AND am.metric_key='input_power'"""
        ).fetchone()

        self.assertEqual(row["sample_count"], 1)
        self.assertAlmostEqual(row["coverage_pct"], 100.0, places=6)
        self.assertAlmostEqual(row["energy_wh"], 100 / 60, places=6)

    def test_measured_zero_is_not_missing(self):
        self.observation("2026-09-24T22:00:05.000Z", 0)
        self.conn.commit()

        aggregate_at(
            self.conn,
            "1min",
            datetime(2026, 9, 24, 22, 0, tzinfo=timezone.utc),
        )

        row = self.conn.execute(
            """SELECT value_avg,state
               FROM aggregate_measurement am
               JOIN aggregation_run ar ON ar.aggregation_run_id=am.aggregation_run_id
               WHERE ar.layer='1min'
                 AND am.metric_key='input_power'"""
        ).fetchone()

        self.assertEqual(row["value_avg"], 0.0)
        self.assertEqual(row["state"], "measured")

    def test_port_measurements_are_aggregated(self):
        obs = self.observation("2026-09-24T22:00:05.000Z")
        self.conn.execute(
            """INSERT INTO device_port(device_id,port_type,port_index)
               VALUES (?,?,?)""",
            (self.device, "usb", 0),
        )
        port = self.conn.execute(
            """SELECT port_id FROM device_port
               WHERE device_id=? AND port_type='usb' AND port_index=0""",
            (self.device,),
        ).fetchone()[0]
        add_port_measurement(
            self.conn,
            observation_id=obs,
            port_id=port,
            metric_key="enabled",
            value=True,
            state="measured",
        )
        self.conn.commit()

        aggregate_at(
            self.conn,
            "1min",
            datetime(2026, 9, 24, 22, 0, tzinfo=timezone.utc),
        )

        row = self.conn.execute(
            """SELECT subject_type,subject_id,metric_key,value_avg,state
               FROM aggregate_measurement am
               JOIN aggregation_run ar ON ar.aggregation_run_id=am.aggregation_run_id
               WHERE ar.layer='1min' AND am.subject_type='port'"""
        ).fetchone()

        self.assertEqual(row["subject_type"], "port")
        self.assertEqual(row["subject_id"], port)
        self.assertEqual(row["metric_key"], "enabled")
        self.assertEqual(row["value_avg"], 1.0)
        self.assertEqual(row["state"], "measured")


if __name__ == "__main__":
    unittest.main()
