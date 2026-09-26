"""Generate human-readable Markdown reports from collected HFO data.

Raw fetched data remains authoritative. This module only writes derived files
under Database/WEATHER/Hawai'i/reports.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from core import hst_time
from core.manifest import Manifest

REPORTS_DIRNAME = "reports"
AGGREGATE_FILENAME = "Hawaii_State_Weather_Report.md"
_EXCLUDED_PREFIXES = ("alerts_", "wwamap_", "nhc_current_storms", "ndfd_", "obhistory_")
_EXCLUDED_IDS = {"rain_summary_graphical"}


def _load_resource_names() -> dict[str, str]:
    path = Path(__file__).resolve().parent.parent / "config" / "resources.yaml"
    with path.open(encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    names: dict[str, str] = {}

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if "id" in node and "name" in node:
                names[str(node["id"])] = str(node["name"])
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(config)
    return names


def _display_name(resource_id: str, names: dict[str, str]) -> str:
    if resource_id in names:
        return names[resource_id]
    for base_id, name in names.items():
        if resource_id.startswith(base_id + "_"):
            return "{} — {}".format(name, resource_id[len(base_id) + 1:])
    return resource_id.replace("_", " ").title()


def _is_reportable(resource_id: str, state_url: str, path: Path) -> bool:
    if resource_id in _EXCLUDED_IDS:
        return False
    if any(resource_id.startswith(prefix) for prefix in _EXCLUDED_PREFIXES):
        return False
    if path.suffix.lower() not in {".txt", ".html", ".json"}:
        return False
    if path.suffix.lower() == ".json":
        return "api.weather.gov/products/" in state_url
    return True


def _extract_report_text(path: Path) -> str | None:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    if path.suffix.lower() != ".json":
        return raw.strip() or None

    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        return None

    def find_product_text(node: Any) -> str | None:
        if isinstance(node, dict):
            value = node.get("productText")
            if isinstance(value, str) and value.strip():
                return value.strip()
            for child in node.values():
                found = find_product_text(child)
                if found:
                    return found
        elif isinstance(node, list):
            for child in node:
                found = find_product_text(child)
                if found:
                    return found
        return None

    return find_product_text(obj)


def _header(title: str, source_url: str, fetched_at: str | None) -> str:
    return "\n".join([
        "# {}".format(title),
        "",
        "> **Official NWS Hawaii/HFO report — derived locally from collected source data.**",
        "",
        "- **Source:** {}".format(source_url),
        "- **Collected:** {} HST".format(fetched_at or "Unknown"),
        "- **Raw source:** retained separately in the weather data tree.",
        "",
        "---",
        "",
    ])


def _as_indented_text(body: str) -> str:
    return "\n".join("    " + line if line else "    " for line in body.splitlines())


def generate(base_dir: str) -> list[Path]:
    """Generate per-product Markdown reports and one statewide aggregate."""
    base = Path(base_dir)
    reports_dir = base.parent / REPORTS_DIRNAME
    reports_dir.mkdir(parents=True, exist_ok=True)

    manifest = Manifest(base_dir).load()
    names = _load_resource_names()

    # Remove only stale generated Markdown files. Raw source data is never
    # touched. The next pass recreates the complete current report set.
    expected = {AGGREGATE_FILENAME}
    for resource_id in manifest.all_states():
        expected.add("{}_current.md".format(resource_id))
    for old in reports_dir.glob("*_current.md"):
        if old.name not in expected:
            old.unlink()
    sections: list[tuple[str, str, str, str | None, str]] = []

    for resource_id, state in manifest.all_states().items():
        local_dir = base / state.local_resource_dir
        if not local_dir.is_dir():
            continue

        candidates = sorted(p for p in local_dir.glob("*_current.*") if p.is_file())
        if not candidates:
            continue
        current_path = candidates[0]

        if not _is_reportable(resource_id, state.url, current_path):
            continue

        body = _extract_report_text(current_path)
        if not body:
            continue

        title = _display_name(resource_id, names)
        report = (
            _header(title, state.url, state.current_fetch_timestamp_hst)
            + _as_indented_text(body)
            + "\n"
        )
        (reports_dir / "{}_current.md".format(resource_id)).write_text(report, encoding="utf-8")
        sections.append((resource_id, title, state.url, state.current_fetch_timestamp_hst, body))

    sections.sort(key=lambda item: (item[1].lower(), item[0].lower()))

    now = hst_time.hst_now().isoformat(timespec="seconds")
    aggregate: list[str] = [
        "# Hawaii State Weather Report",
        "",
        "> **Official NWS Hawaii/HFO statewide collection — generated automatically from locally collected current reports.**",
        "",
        "- **Generated:** {} HST".format(now),
        "- **Current report sections:** {}".format(len(sections)),
        "- **Raw source data:** retained separately; this document is derived and may be regenerated at any time.",
        "",
        "---",
        "",
    ]

    for index, (resource_id, title, source_url, fetched_at, body) in enumerate(sections, 1):
        aggregate.extend([
            "## {}. {}".format(index, title),
            "",
            "- **Resource ID:** {}".format(resource_id),
            "- **Source:** {}".format(source_url),
            "- **Collected:** {} HST".format(fetched_at or "Unknown"),
            "",
            _as_indented_text(body),
            "",
            "---",
            "",
        ])

    aggregate_path = reports_dir / AGGREGATE_FILENAME
    aggregate_path.write_text("\n".join(aggregate), encoding="utf-8")
    return [reports_dir / "{}_current.md".format(resource_id) for resource_id, *_ in sections] + [aggregate_path]
