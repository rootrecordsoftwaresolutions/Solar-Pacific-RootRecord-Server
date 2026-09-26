# 🌺 RootRecord Weather Database

> **Continuously updated, source-preserving weather data and media collected by the RootRecord weather system for Hawaiʻi.**

## 🛰️ Live GOES-18 Hawaii GeoColor

![GOES-18 Hawaii GeoColor]({{README_BANNER_URL}})

## 🌐 What This Is

This repository contains the weather data and media collected by the RootRecord weather system.

Tracked content includes current products, archived products, JSON, HTML, text, satellite imagery, weather graphics, GIFs, hurricane data, reports, and database metadata.

The raw collected source material remains the authoritative local record. Generated reports are derived presentation layers and do not replace the original source data.

## 📚 Report Layers

- **Official Sources** — readable official-source records grouped by issuing source.
- **0 Level Processing** — statewide Hawaiʻi reporting.
- **1 County Processing** — deterministically routed county/geographic reporting.
- **Archives** — historical versions retained when substantive report content changes.

## 🔄 Automatic Updating

Weather reports and media are generated locally from the collected database and published through the existing RootRecord Git synchronization workflow.

This README is also regenerated automatically from the same current statewide report sections used by the weather reporting pipeline.

## 🛡️ Source Integrity

- Original source identity is retained.
- Raw source material is preserved separately from generated reports.
- Official-source records remain isolated from processing levels.
- County routing uses deterministic geographic rules.
- Products without authoritative geographic assignment are not silently copied into counties.
- Current reports are archived when substantive content changes.

---

{{LIVE_REPORT}}

---

_Generated automatically by the RootRecord weather reporting pipeline._
