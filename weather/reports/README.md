# Hawaii State Weather Reporting

> **A source-preserving, continuously updating weather-reporting layer for Hawaiʻi — designed from the start to expand to other regions and eventually global coverage.**

![Status](https://img.shields.io/badge/status-active-2ea44f?style=flat-square) ![Focus](https://img.shields.io/badge/current%20coverage-Hawaiʻi-1f6feb?style=flat-square) ![Processing](https://img.shields.io/badge/processing-deterministic-6f42c1?style=flat-square)

## 🌺 What this is

This directory contains the human-readable reporting layer built from the collected weather data for Hawaiʻi.

**Preserve the official source first. Process it second. Never lose provenance.**

The current deployment is Hawaiʻi-focused. The architecture is intentionally location-aware rather than Hawaii-hardcoded, so additional states, regions, countries, and customer-specific locations can be introduced without changing the fundamental source/provenance model.

## 📡 Current statewide report

The primary statewide output is:

    0 Level Processing/Hawaii_State_Weather_Report_current.md

It is regenerated from the collected data as the underlying products change. Previous versions are retained in the Level 0 archive when the report content actually changes.

## 🗂️ Reporting architecture

```text
Collected Official Data
        │
        ├──────────────► Official Sources
        │                 ├── NWS-HFO
        │                 ├── NHC
        │                 ├── NOAA
        │                 └── NOAA-NESDIS / NOAA-GML
        │
        ▼
0 Level Processing
        │
        ▼
1 County Processing
        │
        ├── Honolulu
        ├── Hawaii
        ├── Maui
        ├── Kauai
        └── Kalawao
        │
        └── unresolved/  ← retained, never silently assigned
```

### Why the separation matters

The same weather product can be useful to several downstream consumers, but the system must not blur the distinction between what an official source said, what statewide processing extracted, what geographic rules assigned to a county, and what a future application may infer.

That separation is especially important for automated and local-LLM consumers.

## 🏛️ Official Sources

Official readable products are preserved outside the processing levels under:

    Official Sources/<source>/

Each source maintains its own current/archive lifecycle.

| Source | Purpose |
|---|---|
| **NWS-HFO** | National Weather Service Hawaiʻi Forecast Office and weather.gov products |
| **NHC** | National Hurricane Center products |
| **NOAA** | NOAA-hosted source material |
| **NOAA-GML** | NOAA Geophysical Monitoring / solar-calculation source material |
| **NOAA-NESDIS** | NESDIS-hosted material when represented as reportable products |

The official-source Markdown records are readable representations of collected source products, **not AI summaries**.

## 🧭 Geographic processing

Level 1 uses deterministic geographic assignment. Authoritative NWS zone/county relationships are preferred, followed by explicit county UGCs and documented routing rules.

If geography cannot be established safely, the product is retained under:

    1 County Processing/unresolved/

It is **not copied into every county** merely because the system cannot determine where it belongs. Explicitly statewide resources are the exception and are intentionally included in every county.

NWS provides zone/county correlation data for this purpose, and its API supports alert retrieval by state, county, and forecast zone. urlNWS GIS Zone/County resourceshttps://www.weather.gov/gis/ZoneCounty · urlNWS API documentationhttps://www.weather.gov/documentation/services-web-api

## 🕒 Current vs. archived reports

Current products use _current.md filenames.

When a product's substantive content changes, the previous current version is moved into archived/ using its original report-creation timestamp, and the new version becomes current. Timestamp-only regeneration does not create unnecessary archive versions.

Raw source data is not replaced by the reporting layer.

## 🌎 Designed to grow beyond Hawaiʻi

Hawaiʻi is the current deployment because it is the first fully developed geographic coverage area. The long-term structure can support a hierarchy such as:

```text
Global
├── United States
│   ├── Hawaiʻi
│   │   ├── statewide
│   │   └── counties / local areas
│   ├── Mainland server coverage
│   │   └── selected states / regions
│   └── special-interest locations
├── Pacific
├── Americas
├── Europe
├── Asia
└── other global regions
```

This lets the public GitHub project remain focused instead of becoming a giant dump of every location. Customer-facing location coverage, mainland infrastructure, and special-interest datasets can remain appropriately separated while sharing the same underlying architecture.

## 🤖 Built for machines and humans

The reports are Markdown because they are easy for people to read, easy to archive and diff, and straightforward for local automation or LLM-based systems to consume.

The system intentionally avoids using an AI model to decide geographic ownership of a source product. Geographic assignment is deterministic and auditable.

## 🔐 Data integrity principles

- **Official data is preserved.**
- **Raw source data is not rewritten by the report layer.**
- **Source identity is retained.**
- **Processing levels remain separate.**
- **Geographic assignment is deterministic.**
- **Unresolved geography is never silently duplicated.**
- **Current and historical report versions are retained.**
- **Derived reports identify their source layer.**
- **The architecture is location-scalable.**

## 🧪 Verification

The repository includes a dependency-light test runner so reporting and scheduler logic can be verified without pytest.

The latest verified baseline before the most recent documentation/test-harness commits was **82 passing, 0 failing, 0 errors**. Run the local suite after pulling the latest main branch before treating a new deployment as verified.

## 📁 Related documentation

- weather/BUILD_STATUS.md — implementation status and remaining work
- weather/reports/ — current reporting architecture
- weather/config/ — geographic and resource configuration
- weather/discovery/ — deterministic hazard/source discovery
- weather/fetch/ — source collection modules
- weather/core/ — shared collection, archival, manifest, and HTTP infrastructure

---

### Project direction

**Start with Hawaiʻi. Preserve the source. Make every transformation auditable. Expand the same architecture wherever the data needs to go.**
