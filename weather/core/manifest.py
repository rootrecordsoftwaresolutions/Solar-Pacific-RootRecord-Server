"""Per-resource state tracking (etag, hash, fetch timestamps, failures).

Single JSON file per nws_plan.md Section 6: `hfo/_manifest.json`. This module
only reads/writes that state -- it has no opinion on what "changed" means
(that's core/change_detection.py) and makes no HTTP calls of its own.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any


MANIFEST_FILENAME = "_manifest.json"


@dataclass
class ResourceState:
    resource_id: str
    url: str
    local_resource_dir: str
    current_fetch_timestamp_hst: str | None = None  # ISO string, HST
    etag: str | None = None
    last_modified: str | None = None
    content_length: int | None = None
    content_sha256: str | None = None
    consecutive_failures: int = 0
    last_failure_at: str | None = None
    last_success_at: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "ResourceState":
        known = {f: d.get(f) for f in cls.__dataclass_fields__}
        return cls(**known)


class Manifest:
    """Loads/holds/saves the full `_manifest.json` for one base_dir (e.g. `hfo/`)."""

    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.path = Path(base_dir) / MANIFEST_FILENAME
        self._data: dict[str, ResourceState] = {}

    def load(self) -> "Manifest":
        if self.path.is_file():
            try:
                raw = json.loads(self.path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                raw = {}
            self._data = {
                rid: ResourceState.from_dict(entry) for rid, entry in raw.items()
            }
        return self

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        serializable = {rid: state.to_dict() for rid, state in self._data.items()}
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(serializable, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(self.path)  # atomic-ish swap, avoid a torn manifest on crash

    def get(self, resource_id: str) -> ResourceState | None:
        return self._data.get(resource_id)

    def get_or_create(self, resource_id: str, url: str, local_resource_dir: str) -> ResourceState:
        state = self._data.get(resource_id)
        if state is None:
            state = ResourceState(resource_id=resource_id, url=url, local_resource_dir=local_resource_dir)
            self._data[resource_id] = state
        return state

    def record_success(self, resource_id: str, *, etag: str | None, last_modified: str | None,
                        content_length: int | None, content_sha256: str | None,
                        fetched_at_hst_iso: str) -> None:
        state = self._data[resource_id]
        state.etag = etag
        state.last_modified = last_modified
        state.content_length = content_length
        state.content_sha256 = content_sha256
        state.current_fetch_timestamp_hst = fetched_at_hst_iso
        state.consecutive_failures = 0
        state.last_success_at = fetched_at_hst_iso

    def record_unchanged(self, resource_id: str, *, confirmed_at_hst_iso: str) -> None:
        """A 304/matched-hash result -- update the 'still fresh' timestamp only.

        Per nws_plan.md Section 3, this does NOT touch current_fetch_timestamp_hst
        (that stays as the timestamp of the version actually on disk, which is
        what archiver.py needs when the NEXT real change is detected).
        """
        state = self._data[resource_id]
        state.last_success_at = confirmed_at_hst_iso
        state.consecutive_failures = 0

    def record_failure(self, resource_id: str, *, failed_at_hst_iso: str) -> None:
        state = self._data[resource_id]
        state.consecutive_failures += 1
        state.last_failure_at = failed_at_hst_iso

    def all_states(self) -> dict[str, ResourceState]:
        return dict(self._data)
