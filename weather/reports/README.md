# Hawaii Weather Reports

The report layer is derived from the collected NWS Hawaii Forecast Office
(HFO) data under:

\`/home/rootrecord/Database/WEATHER/Hawai'i/hfo\`

Reports are written beside that source tree:

\`/home/rootrecord/Database/WEATHER/Hawai'i/reports\`

## Outputs

- \`Hawaii_State_Weather_Report_current.md\` — one combined statewide report.
- \`<resource_id>_current.md\` — one readable Markdown report per current official
  text product.

The scheduler regenerates these reports after each dispatch pass.

## Raw data

Raw official HTML responses are retained automatically when an HTTP response
is HTML. The parsed/cleaned product remains the normal current/archive
artifact, while the raw HTML is kept in that resource's \`raw/\` companion
directory.

The report layer never deletes or rewrites raw source data.
