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

A GOES imagery banner will be selected from the live GOES-18 Hawaii or GOES-19 East Pacific products once the imagery feed is confirmed working. The banner choice is intentionally left open so the most useful current visualization can be selected from the collected products.

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

The README update is intentionally **local-first**. Generating a new report does not automatically commit or push to GitHub. Publication can be synchronized separately so data collection remains independent from Git operations.

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
