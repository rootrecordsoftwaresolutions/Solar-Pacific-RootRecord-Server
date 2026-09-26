# Hawaii Weather Reports

The report layer is derived from the collected NWS Hawaii Forecast Office
(HFO) data under:

\`/home/rootrecord/Database/WEATHER/Hawai'i/hfo\`

Reports are written into the first organized processing layer:

\`/home/rootrecord/Database/WEATHER/Hawai'i/reports/0 Level Processing\`

## Outputs

- \`Hawaii_State_Weather_Report_current.md\` — one combined statewide report.
- \`<resource_id>_current.md\` — one readable Markdown report per current official
  text product.
- \`archived/\` — previous report versions, retained using the report's original
  creation timestamp.

The scheduler regenerates these reports after each dispatch pass.

## Raw data

Raw official HTML responses are retained automatically when an HTTP response
is HTML. The parsed/cleaned product remains the normal current/archive
artifact, while the raw HTML is kept in that resource's \`raw/\` companion
directory.

The report layer never deletes or rewrites raw source data.

## Level 0 processing

Level 0 is the first organized report layer extracted from the raw weather data. It intentionally remains broad and unclassified; later processing levels can consume these readable reports without changing the raw-data layer.

Current reports remain named with `_current.md`. When a report actually changes, the previous current version is moved into `archived/` using the timestamp recorded when that version was created. Unchanged reports are not re-archived.


## Level 1 county processing

Level 1 is a deterministic geographic processing layer. It may use the preserved Official Sources record when its resource ID and authoritative source URL match the Level 0 record; otherwise it uses the Level 0 record. It never modifies or replaces Level 0.

Reports are written under:

`/home/rootrecord/Database/WEATHER/Hawai'i/reports/1 County Processing`

The county layer is deterministic and uses explicit geographic rules, resource
routing, county aliases, and later geographic datasets such as NWS shapefiles.
It does not use AI/LLM classification.

Each county gets:

- a directory containing an individual `<resource_id>_current.md` for every
  deterministically assigned source record;
- a county aggregate named
  `<county>_County_Weather_Report_current.md`;
- previous versions are archived in the Level-1 `archived/` directory using
  the original report-creation timestamp.

Statewide resources explicitly configured as statewide are included in every county. If a source cannot be assigned geographically by an authoritative UGC/zone rule, explicit resource rule, or documented text rule, Level 1 preserves it under `unresolved/` and excludes it from every county. This prevents ambiguous geography from being silently copied into multiple counties.

This makes every processing level independently reproducible and independently
archivable.


## Official-source preservation

Official readable weather products are also mirrored outside the processing
levels so the source identity is never lost.

Reports are organized under:

`/home/rootrecord/Database/WEATHER/Hawai'i/reports/Official Sources/<source>/`

Current source groups include:

- `NWS-HFO/` — NWS Hawaii Forecast Office products and weather.gov forecast products.
- `NHC/` — National Hurricane Center products.
- `NOAA/` — NOAA-hosted source material.
- `NOAA-NESDIS/` — NESDIS-hosted imagery/source material when represented as reports.\n- `NOAA-GML/` — NOAA Geophysical Monitoring for Climate/solar-calculation source material.

Each source has its own `archived/` directory and independent current/archive
lifecycle. A change to an NWS-HFO product therefore does not age or overwrite
an NHC product, and neither source is treated as part of a processing level.

The exact fetched official bytes remain in the URL-mirrored raw weather-data
tree. The source-isolated Markdown layer is the readable official-product
representation; it is not an AI summary or interpretation.

## GIS source preservation

The GIS fetcher preserves both the authoritative NWS GIS catalog page and the
versioned artifact selected from that catalog. This is important because NWS
publishes versioned county, public-zone, zone/county-correlation, CWA, fire-zone,
and marine-zone datasets. The catalog itself is retained as evidence of what
version was available when the fetch occurred.

NWS documents public forecast zones as polygon data and notes that zones may be
subsets of counties; its Zone/County correlation file provides the corresponding
county/FIPS relationship. The Level 1 county processor uses those authoritative
relationships before falling back to less-specific routing rules.

## Provenance boundary

The processing layers are intentionally separated from the Official Sources preservation layer. Official-source Markdown is generated directly from the collected source resource and never from Level 0. Level 1 records identify their `Source layer` and `County assignment`; unresolved products are never copied into county directories. This keeps source identity and geographic assignment auditable for downstream local-LLM use.
