"""Build source-isolated mirrors of official report products.

This is NOT a processing level. It is a preservation/organization layer that
keeps official-source reports grouped by issuing source while Level 0 and
Level 1 remain processing layers.

The exact fetched source bytes remain in the URL-mirrored raw data tree.
These Markdown files are the readable official-product representation.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlsplit

from core import hst_time

ROOT = "reports"
OFFICIAL = "Official Sources"
LEVEL0 = "0 Level Processing"
ARCHIVE = "archived"


def _source_name(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    if host in {"api.weather.gov", "www.weather.gov", "forecast.weather.gov"}:
        return "NWS-HFO"
    if host in {"www.nhc.noaa.gov", "nhc.noaa.gov"}:
        return "NHC"
    if host in {"www.noaa.gov", "noaa.gov"}:
        return "NOAA"
    if "nesdis.noaa.gov" in host:
        return "NOAA-NESDIS"
    return re.sub(r"[^A-Za-z0-9._-]+", "_", host or "unknown-source")


def _created(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = re.search(r"^- \*\*Report created:\*\* (.+?) HST$", text, re.M)
    return m.group(1).strip() if m else None


def _archive(path: Path, archive_dir: Path, fallback: str) -> None:
    if not path.is_file():
        return
    stamp = re.sub(r"[^0-9A-Za-z:+-]", "-", _created(path) or fallback).strip("-")
    stem = path.name.removesuffix("_current.md")
    target = archive_dir / f"{stem}_{stamp}.md"
    n = 2
    while target.exists():
        target = archive_dir / f"{stem}_{stamp}_{n}.md"
        n += 1
    archive_dir.mkdir(parents=True, exist_ok=True)
    path.replace(target)


def _normalize_for_compare(text: str) -> str:
    return re.sub(
        r"^- \*\*Generated:\*\* .+? HST$",
        "- **Generated:** <timestamp> HST",
        text,
        flags=re.M,
    )


def _write(path: Path, content: str, archive_dir: Path, created: str) -> bool:
    if path.is_file():
        try:
            old = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            old = ""
        if _normalize_for_compare(old) == _normalize_for_compare(content):
            return False
        _archive(path, archive_dir, created)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _body(text: str) -> str:
    fence = chr(96) * 3
    m = re.search(re.escape(fence) + r"text\n(.*?)\n" + re.escape(fence), text, re.S)
    return m.group(1).strip() if m else text.strip()


def generate(base_dir: str) -> list[Path]:
    base = Path(base_dir)
    reports_root = base.parent / ROOT
    level0 = reports_root / LEVEL0
    official_root = reports_root / OFFICIAL
    now = hst_time.hst_now().isoformat(timespec="seconds")
    outputs: list[Path] = []

    if not level0.is_dir():
        return outputs

    for path in sorted(level0.glob("*_current.md")):
        if path.name == "Hawaii_State_Weather_Report_current.md":
            continue
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        source_match = re.search(r"^- \*\*Source:\*\* (.+)$", raw, re.M)
        source_url = source_match.group(1).strip() if source_match else ""
        if not source_url.startswith(("http://", "https://")):
            continue

        source = _source_name(source_url)
        resource_id = path.name.removesuffix("_current.md")
        title_match = re.search(r"^# (.+)$", raw, re.M)
        title = title_match.group(1).strip() if title_match else resource_id.replace("_", " ").title()
        body = _body(raw)

        source_dir = official_root / source
        archive_dir = source_dir / ARCHIVE
        target = source_dir / f"{resource_id}_current.md"
        fence = chr(96) * 3
        content = "\n".join([
            f"# {title}",
            "",
            "> **Official-source report mirror.** This is organized by issuing source, not a processing level.",
            "",
            f"- **Generated:** {now} HST",
            f"- **Report created:** {now} HST",
            f"- **Source authority:** {source}",
            f"- **Resource ID:** {resource_id}",
            f"- **Official source:** {source_url}",
            "- **Processing:** none; this layer preserves the readable official-product representation.",
            "- **Raw source:** retained separately in the URL-mirrored weather data tree.",
            "- **Level 0:** remains a separate processing layer and is not modified here.",
            "",
            "---",
            "",
            fence + "text",
            body,
            fence,
            "",
        ])
        _write(target, content, archive_dir, now)
        outputs.append(target)

    return outputs
