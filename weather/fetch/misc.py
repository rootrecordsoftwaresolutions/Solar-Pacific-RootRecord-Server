"""Static/miscellaneous weather resources that do not fit text/image categories."""
from __future__ import annotations
from core.manifest import Manifest
from fetch import _engine

def fetch_all(manifest: Manifest, base_dir: str) -> list[_engine.FetchOutcome]:
    config = _engine.load_resources_yaml()
    outcomes = []
    for item in config.get("misc", []):
        outcomes.append(_engine.run_resource(
            manifest, base_dir, item["id"], item["url"],
            method=item.get("method", "binary"),
            expected_ext=item.get("expected_ext"),
        ))
    return outcomes
