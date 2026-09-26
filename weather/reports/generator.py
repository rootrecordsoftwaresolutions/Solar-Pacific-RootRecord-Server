"""Generate human-readable Markdown reports from collected HFO data.

Raw fetched data remains authoritative. This module only writes derived files
under Database/WEATHER/Hawai'i/reports.
"""
from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml

from core import hst_time
from core.manifest import Manifest

REPORTS_DIRNAME = "reports"
LEVEL0_DIRNAME = "0 Level Processing"
ARCHIVE_DIRNAME = "archived"
AGGREGATE_FILENAME = "Hawaii_State_Weather_Report_current.md"
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


class _VisibleTextParser(HTMLParser):
    """Extract visible HTML text while preserving useful line structure."""

    _BLOCK_TAGS = {
        "address", "article", "aside", "blockquote", "br", "dd", "div", "dl",
        "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2",
        "h3", "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "ol",
        "p", "pre", "section", "table", "td", "th", "tr", "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "template"}:
            self._skip_depth += 1
            return
        if not self._skip_depth and tag in self._BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "template"}:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if not self._skip_depth and tag in self._BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self.parts.append(data)


def _html_to_text(raw: str) -> str:
    """Extract the actual visible NWS report from an HTML response."""
    pre_matches = re.findall(r"<pre\b[^>]*>(.*?)</pre\s*>", raw, flags=re.I | re.S)
    if pre_matches:
        return html.unescape(re.sub(r"<[^>]+>", "", pre_matches[-1])).strip()

    parser = _VisibleTextParser()
    try:
        parser.feed(raw)
        parser.close()
        text = html.unescape("".join(parser.parts))
    except Exception:
        text = html.unescape(re.sub(r"<[^>]+>", "", raw))

    lines = [re.sub(r"[ \\t]+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(lines).strip()


def _extract_report_text(path: Path) -> str | None:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    if not raw.strip():
        return None

    if path.suffix.lower() == ".html":
        return _html_to_text(raw) or None

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


def _header(title: str, source_url: str, fetched_at: str | None, created_at: str) -> str:
    return "\n".join([
        "# {}".format(title),
        "",
        "> **Official NWS Hawaii/HFO report — derived locally from collected source data.**",
        "",
        "- **Source:** {}".format(source_url),
        "- **Collected:** {} HST".format(fetched_at or "Unknown"),
        "- **Report created:** {} HST".format(created_at),
        "- **Raw source:** retained separately in the weather data tree.",
        "",
        "---",
        "",
    ])


def _as_markdown_report(body: str) -> str:
    """Preserve fixed-width NWS formatting without Markdown mangling it."""
    fence = "`" * 3
    body = body.replace(fence, "[NWS-FENCE]")
    return fence + "text\n" + body.rstrip() + "\n" + fence


def _existing_created_at(path: Path) -> str | None:
    """Read the report creation timestamp before it is replaced."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    match = re.search(r"^- \\*\\*Report created:\\*\\* (.+?) HST$", raw, flags=re.M)
    return match.group(1).strip() if match else None


def _archive_current(current_path: Path, archive_dir: Path, fallback_created_at: str) -> None:
    """Archive an existing current report using its original creation timestamp."""
    if not current_path.is_file():
        return
    created_at = _existing_created_at(current_path) or fallback_created_at
    safe_timestamp = re.sub(r"[^0-9A-Za-z:+-]", "-", created_at).strip("-")
    stem = current_path.name.removesuffix("_current.md")
    archive_path = archive_dir / (stem + "_" + safe_timestamp + ".md")
    if archive_path.exists():
        index = 2
        while True:
            candidate = archive_dir / (stem + "_" + safe_timestamp + "_" + str(index) + ".md")
            if not candidate.exists():
                archive_path = candidate
                break
            index += 1
    archive_dir.mkdir(parents=True, exist_ok=True)
    current_path.replace(archive_path)


def _write_current(current_path: Path, content: str, archive_dir: Path, created_at: str) -> None:
    """Write current, archiving the previous version only when content changed."""
    if current_path.is_file():
        try:
            existing = current_path.read_text(encoding="utf-8", errors="replace")
            comparable_existing = re.sub(
                r"^- \\*\\*Generated:\\*\\* .+? HST$",
                "- **Generated:** <timestamp> HST",
                existing,
                flags=re.M,
            )
            comparable_content = re.sub(
                r"^- \\*\\*Generated:\\*\\* .+? HST$",
                "- **Generated:** <timestamp> HST",
                content,
                flags=re.M,
            )
            if comparable_existing == comparable_content:
                return
        except OSError:
            pass
        _archive_current(current_path, archive_dir, created_at)
    current_path.parent.mkdir(parents=True, exist_ok=True)
    current_path.write_text(content, encoding="utf-8")


def generate(base_dir: str) -> list[Path]:
    """Generate level-0 per-product Markdown reports and one statewide aggregate."""
    base = Path(base_dir)
    reports_root = base.parent / REPORTS_DIRNAME
    reports_dir = reports_root / LEVEL0_DIRNAME
    archive_dir = reports_dir / ARCHIVE_DIRNAME
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
    now = hst_time.hst_now().isoformat(timespec="seconds")

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
        current_path = reports_dir / "{}_current.md".format(resource_id)
        created_at = now
        report = (
            _header(title, state.url, state.current_fetch_timestamp_hst, created_at)
            + _as_markdown_report(body)
            + "\n"
        )
        _write_current(current_path, report, archive_dir, now)
        sections.append((resource_id, title, state.url, state.current_fetch_timestamp_hst, body))

    sections.sort(key=lambda item: (item[1].lower(), item[0].lower()))

    aggregate_created_at = now
    aggregate: list[str] = [
        "# Hawaii State Weather Report",
        "",
        "> **Official NWS Hawaii/HFO statewide collection — generated automatically from locally collected current reports.**",
        "",
        "- **Generated:** {} HST".format(now),
        "- **Report created:** {} HST".format(aggregate_created_at),
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
            _as_markdown_report(body),
            "",
            "---",
            "",
        ])

    aggregate_path = reports_dir / AGGREGATE_FILENAME
    _write_current(aggregate_path, "\n".join(aggregate), archive_dir, now)
    return [reports_dir / "{}_current.md".format(resource_id) for resource_id, *_ in sections] + [aggregate_path]
