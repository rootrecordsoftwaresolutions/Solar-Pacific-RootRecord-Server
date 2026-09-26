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
