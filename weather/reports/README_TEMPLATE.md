# 🌺 Hawaiʻi State Weather Database

> **RootRecord's continuously updated, source-preserving weather database and reporting layer for Hawaiʻi.**

## 🌐 What This Is

This directory is the human-readable reporting layer built from the locally collected Hawaiʻi weather database.

The system is designed around a strict separation between:

- **Raw collected data** — the original fetched source material remains authoritative.
- **Official Sources** — readable copies preserved by issuing source, without processing-level mixing.
- **0 Level Processing** — statewide readable reports.
- **1 County Processing** — deterministic county/geographic reports.
- **Archives** — prior report versions are retained when substantive source content changes.

The live report below is regenerated automatically from the current statewide report data. It is not manually maintained.

## 🛰️ Imagery

![GOES-18 Hawaii GeoColor](https://raw.githubusercontent.com/rootrecordsoftwaresolutions/RootRecord-Weather-Database/main/Hawai%27i/hfo/cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/hi/GEOCOLOR/GOES18-HI-GEOCOLOR-600x600/GOES18-HI-GEOCOLOR-600x600_current.gif)

**GOES-18 Hawaii — GeoColor** is the selected live README banner. The image is the locally collected `_current.gif` product from the weather database, published through the existing weather-data synchronization pipeline.

The imagery pipeline uses stable NOAA/NESDIS product URLs. The stable URL is fetched repeatedly; when the returned image changes, the previous version is archived and the current product keeps its real source filename followed by `_current`.

## 🧭 Data Architecture

```text
Official / NOAA / NWS / NESDIS sources
                │
                ▼
        Raw Weather Database
                │
                ├──────────────► Official Sources
                │                    │
                ▼                    ▼
          0 Level Processing ───► 1 County Processing
                │                    │
                └──────────────┬─────┘
                               ▼
                     Live README / Reports
```

### Source integrity

- Original source identity is retained.
- Raw source material is not replaced by generated reports.
- Official-source records remain isolated from processing levels.
- County routing uses deterministic geographic rules.
- Products without authoritative geographic assignment are not silently copied into counties.
- Current reports are archived when substantive content changes.
- The live README and statewide report are generated from the same current product sections.

## 📚 Report Layers

| Layer | Purpose |
|---|---|
| **Official Sources** | Preserve readable official-source products grouped by issuing source |
| **0 Level Processing** | Statewide Hawaiʻi reporting |
| **1 County Processing** | Deterministically routed county reporting |
| **Archives** | Historical versions of changed reports |

## 🔄 Automatic Updating

Each scheduler/report-generation cycle can regenerate this README locally from the latest collected data.

The README is published through the existing RootRecord Git synchronization workflow alongside the other generated weather/report/media artifacts.

## 🤖 Machine / LLM Use

The database is structured so a local model can consume:

1. raw source material,
2. source-preserved official records,
3. statewide processing,
4. county-level processing,
5. historical archives,

without treating a generated summary as the original source.

## 🛡️ Integrity Boundary

Generated reports are presentation/processing artifacts. The raw collected weather data remains the authoritative local record.

No AI/LLM is used to decide geographic ownership of weather products.

---

{{LIVE_REPORT}}

---

_Generated automatically by the RootRecord weather reporting pipeline._
