"""Deterministic Level-1 county report generator. Level 0 is never modified."""
from __future__ import annotations
import re
from pathlib import Path
from typing import Any
import yaml
from core import hst_time

ROOT = "reports"
LEVEL0 = "0 Level Processing"
LEVEL1 = "1 County Processing"
ARCHIVE = "archived"
CONFIG = "report_counties.yaml"

def _config() -> dict[str, Any]:
    path = Path(__file__).resolve().parent.parent / "config" / CONFIG
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

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

def _write(path: Path, content: str, archive_dir: Path, created: str) -> None:
    if path.is_file():
        try:
            old = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            old = ""
        normalize = lambda s: re.sub(r"^- \*\*Generated:\*\* .+? HST$", "- **Generated:** <timestamp> HST", s, flags=re.M)
        if normalize(old) == normalize(content):
            return
        _archive(path, archive_dir, created)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def _body(text: str) -> str:
    fence = chr(96) * 3
    m = re.search(re.escape(fence) + r"text\n(.*?)\n" + re.escape(fence), text, re.S)
    return m.group(1).strip() if m else text.strip()

def _matches(text: str, counties: dict[str, Any]) -> set[str]:
    found = set()
    for key, cfg in counties.items():
        for alias in cfg.get("aliases", []):
            if re.search(r"(?<![A-Za-z])" + re.escape(str(alias)) + r"(?![A-Za-z])", text, re.I):
                found.add(key)
                break
    return found

def _targets(resource_id: str, body: str, cfg: dict[str, Any]) -> tuple[set[str], str]:
    counties = {str(c["key"]): c for c in cfg.get("counties", [])}
    statewide = set(cfg.get("statewide_resource_ids", []))
    if resource_id in statewide:
        return set(counties), "statewide"
    for county, patterns in cfg.get("resource_routing", {}).get("county_patterns", {}).items():
        if any(re.search(p, resource_id, re.I) for p in patterns):
            return {county}, "explicit-resource"
    found = _matches(body, counties)
    if found:
        return found, "explicit-text"
    return set(counties), "unresolved/statewide-source"

def generate(base_dir: str) -> list[Path]:
    base = Path(base_dir)
    root = base.parent / ROOT
    level0 = root / LEVEL0
    level1 = root / LEVEL1
    archive = level1 / ARCHIVE
    level1.mkdir(parents=True, exist_ok=True)
    cfg = _config()
    counties = {str(c["key"]): c for c in cfg.get("counties", [])}
    buckets = {key: [] for key in counties}
    now = hst_time.hst_now().isoformat(timespec="seconds")

    for path in sorted(level0.glob("*_current.md")):
        if path.name == "Hawaii_State_Weather_Report_current.md":
            continue
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        resource_id = path.name.removesuffix("_current.md")
        source_m = re.search(r"^- \*\*Source:\*\* (.+)$", raw, re.M)
        title_m = re.search(r"^# (.+)$", raw, re.M)
        source = source_m.group(1).strip() if source_m else ""
        title = title_m.group(1).strip() if title_m else resource_id.replace("_", " ").title()
        body = _body(raw)
        targets, scope = _targets(resource_id, body, cfg)
        for county in targets:
            buckets[county].append((resource_id, title, source, scope, body))

    outputs = []
    fence = chr(96) * 3
    for key, county_cfg in counties.items():
        name = str(county_cfg.get("display_name") or county_cfg.get("speech") or key.title())
        sections = sorted(buckets[key], key=lambda x: (x[1].lower(), x[0].lower()))
        lines = [
            f"# {name} Weather Report", "",
            "> **Level 1 county report — deterministically derived from Level 0.**", "",
            f"- **Generated:** {now} HST",
            f"- **Report created:** {now} HST",
            f"- **County:** {name}",
            f"- **Source level:** {LEVEL0}",
            "- **Processing:** deterministic rules only; no AI/LLM classification.",
            "- **Level 0:** untouched; its current and archived reports remain intact.",
            "", "---", ""
        ]
        for i, (rid, title, source, scope, body) in enumerate(sections, 1):
            lines += [
                f"## {i}. {title}", "",
                f"- **Resource ID:** {rid}",
                f"- **Source:** {source or 'Level 0 report metadata'}",
                f"- **County assignment:** {scope}", "",
                fence + "text", body, fence, "", "---", ""
            ]
        path = level1 / f"{key}_County_Weather_Report_current.md"
        _write(path, "\n".join(lines), archive, now)
        outputs.append(path)
    return outputs
