#!/usr/bin/env python3
"""Initialize the empty RootRecord SQLite schema.

This intentionally creates only schema objects. It does not import, delete,
rewrite, or migrate existing JSON/log/runtime data.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from energy.db.store import DEFAULT_DB_PATH, connect, initialize_schema


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    args = parser.parse_args()

    args.db.parent.mkdir(parents=True, exist_ok=True)
    conn = connect(args.db)
    try:
        initialize_schema(conn)
    finally:
        conn.close()

    print(f"RootRecord schema initialized at {args.db}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
