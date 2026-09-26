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
from urllib.parse import quote
from typing import Any

import yaml

from core import hst_time
from core.manifest import Manifest

from reports.banner import OUTPUT_RELATIVE, generate_readme_banner

REPORTS_DIRNAME = "reports"
LEVEL0_DIRNAME = "0 Level Processing"
ARCHIVE_DIRNAME = "archived"
REPORTING_README = Path(__file__).resolve().parent / "README.md"
DATABASE_README_TEMPLATE = Path(__file__).resolve().parent / "WEATHER_DATABASE_README_TEMPLATE.md"
AGGREGATE_FILENAME = "Hawaii_State_Weather_Report_current.md"
_EXCLUDED_PREFIXES = ("alerts_", "wwamap_", "nhc_current_storms", "ndfd_", "obhistory_")
_EXCLUDED_IDS = {
    "rain_summary_graphical",
    "nhc_source_index",
    "noaa_solar_calculation_table",
    "nws_cwa_boundaries_catalog",
    "nws_fire_zones_catalog",
    "nws_marine_zones_catalog",
    "nws_public_counties_catalog",
    "nws_public_zones_catalog",
    "nws_zone_county_catalog",
}
_README_PLACEHOLDERS = (
    "{{CURRENT_CONDITIONS}}",
    "{{README_BANNER_URL}}",
    "{{REPORT_UPDATED}}",
    "{{REPORT_SECTION_COUNT}}",
    "{{REPORT_SECTIONS}}",
)

# Site chrome phrases that must never appear inside a product body.
_CHROME_MARKERS = (
    "Privacy Policy",
    "Freedom of Information Act",
    "USA.gov",
    "About Us",
    "Career Opportunities",
    "National Weather Service Home",
)


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


def _normalize_inline_whitespace(text: str) -> str:
    """Collapse runs of spaces/tabs to a single space without destroying letters.

    IMPORTANT: never put the letter t into a character class. Use an explicit
    tab character via chr(9) so the source cannot be corrupted by escape
    double-processing.
    """
    tab = chr(9)
    text = text.replace(tab, " ")
    return re.sub(r" +", " ", text).strip()


def _strip_chrome(text: str) -> str:
    """Drop trailing NWS website chrome if it leaked into extracted body text."""
    cut = len(text)
    for marker in _CHROME_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            cut = min(cut, idx)
    return text[:cut].rstrip()


def _pre_product_text(raw: str) -> str | None:
    """Prefer the last <pre> block — that is the official NWS product body."""
    pre_matches = re.findall(r"<pre\b[^>]*>(.*?)</pre\s*>", raw, flags=re.I | re.S)
    if not pre_matches:
        return None
    body = html.unescape(re.sub(r"<[^>]+>", "", pre_matches[-1]))
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    body = _strip_chrome(body)
    return body.rstrip() + ("\n" if body.strip() else "")


def _html_to_text(raw: str, *, preserve_pre: bool = True) -> str:
    """Extract visible text from HTML.

    When a <pre> product block exists, return it verbatim (fixed-width safe).
    Otherwise parse visible text and normalize inline whitespace carefully.
    """
    if preserve_pre:
        pre = _pre_product_text(raw)
        if pre and pre.strip():
            return pre.strip("\n")

    parser = _VisibleTextParser()
    try:
        parser.feed(raw)
        parser.close()
        text = html.unescape("".join(parser.parts))
    except Exception:
        text = html.unescape(re.sub(r"<[^>]+>", "", raw))

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [_normalize_inline_whitespace(line) for line in text.splitlines()]
    cleaned: list[str] = []
    blank_run = 0
    for line in lines:
        if not line:
            blank_run += 1
            if blank_run <= 1:
                cleaned.append("")
            continue
        blank_run = 0
        cleaned.append(line)
    return _strip_chrome("\n".join(cleaned)).strip()


def _extract_report_text(path: Path) -> str | None:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    if not raw.strip():
        return None

    if path.suffix.lower() == ".html":
        text = _html_to_text(raw, preserve_pre=True)
        return text or None

    if path.suffix.lower() != ".json":
        body = raw.replace("\r\n", "\n").replace("\r", "\n")
        body = _strip_chrome(body)
        return body.rstrip() or None

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

    product_text = find_product_text(obj)
    if product_text:
        return _strip_chrome(product_text.replace("\r\n", "\n").replace("\r", "\n")).rstrip()

    if isinstance(obj, dict):
        keys = (
            "productName", "productCode", "issuingOffice", "issuanceTime",
            "wmoCollectiveId", "id", "@id",
        )
        lines = []
        for key in keys:
            value = obj.get(key)
            if value is not None and str(value).strip():
                lines.append("{}: {}".format(key, value))
        if lines:
            return "\n".join(lines)

    return None


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


def _cell_text(raw_cell: str) -> str:
    """Plain text for one table cell — never destroy letter characters."""
    text = re.sub(r"<[^>]+>", " ", raw_cell)
    text = html.unescape(text)
    return _normalize_inline_whitespace(text).replace("|", "\\|")


def _parse_rwr_stations(raw: str) -> dict[str, dict[str, str]]:
    """Map ICAO station id -> observation fields from the HFO RWR HTML table.

    The NWS HFO RWR page publishes each station twice: a Fahrenheit block first,
    then a Celsius block. Keep the FIRST row per ICAO so coastal temps stay in
    °F (e.g. Honolulu 81, not the Celsius twin 27).
    """
    stations: dict[str, dict[str, str]] = {}
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", raw, flags=re.I | re.S):
        icao_match = re.search(
            r"href=[\"'][^\"']*/([A-Z0-9]{4})\.html[\"']",
            row,
            flags=re.I,
        )
        if not icao_match:
            continue
        icao = icao_match.group(1).upper()
        # First table wins (Fahrenheit). Never overwrite with the Celsius twin.
        if icao in stations:
            continue
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", row, flags=re.I | re.S)
        if len(cells) < 7:
            continue
        values = [_cell_text(cell) for cell in cells]
        stations[icao] = {
            "conditions": values[1] or "—",
            "temp": values[2] or "—",
            "dewpoint": values[3] or "—",
            "rh": values[4] or "—",
            "wind": values[5] or "—",
            "pressure": values[6] or "—",
        }
    return stations


def _format_temp_f(value: str) -> str:
    """Render a temperature cell as °F, rejecting obvious Celsius twins."""
    text = (value or "").strip()
    if not text or text == "—":
        return "—"
    match = re.search(r"-?\d+", text)
    if not match:
        return text
    number = int(match.group(0))
    # Coastal Hawaiʻi observations in °F are never in the teens/20s.
    # If we somehow kept a Celsius value, convert it rather than publish nonsense.
    if number < 40:
        number = int(round(number * 9 / 5 + 32))
    return "{}°F".format(number)


def _current_conditions(base: Path) -> str:
    """Build a compact current-conditions table from the collected HFO RWR page."""
    source = base / "weather.gov" / "hfo" / "RWR" / "raw" / "RWR_raw_current.html"
    if not source.is_file():
        return "Current conditions are unavailable from the latest collected HFO observations."

    try:
        raw = source.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "Current conditions are unavailable from the latest collected HFO observations."

    parsed = _parse_rwr_stations(raw)
    stations = [
        ("PHNL", "Honolulu"),
        ("PHLI", "Lihue"),
        ("PHOG", "Kahului"),
        ("PHTO", "Hilo"),
        ("PHKO", "Kona"),
    ]
    rows: list[str] = []
    for icao, label in stations:
        obs = parsed.get(icao)
        if not obs:
            continue
        rows.append(
            "| {} | {} | {} | {} | {}% | {} | {} |".format(
                label,
                obs["conditions"],
                _format_temp_f(obs["temp"]),
                _format_temp_f(obs["dewpoint"]),
                obs["rh"],
                obs["wind"],
                obs["pressure"],
            )
        )

    if not rows:
        return "Current conditions are unavailable from the latest collected HFO observations."

    return "\n".join([
        "| Location | Conditions | Temp | Dew point | RH | Wind | Pressure |",
        "|---|---|---:|---:|---:|---|---:|",
        *rows,
        "",
        "_Source: locally collected NWS-HFO Regional Weather Roundup (RWR). Values are °F._",
    ])
