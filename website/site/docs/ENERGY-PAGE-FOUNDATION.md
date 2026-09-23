# Energy page foundation (Vercel)

- Route: `/energy` on RootRecord Website (Next.js under `skills/website/site`).
- Background: AWS Network Globe at `https://www.rootrecord.cloud` (override with `NEXT_PUBLIC_GLOBE_URL`). **Only AWS hook** on this page.
- Overlay: status-style cards (Solar in, Delta/River SOC, AC out, Buckets, Ports).
- Mainland bypass: energy metrics are not ingested via US-MAINLAND; globe is visual only.
- Desk owner for BLE/scripts: Bruce Monitor (`skills/energy`). Public seal: Carly Mal before visitor-facing polish.
- Bak: `Database/GITHUB/website-site.bak-energy-foundation-*`

## Desk publish contract (Bruce Monitor)

Truth tree: `/home/rootrecord/Database/ENERGY`

| Kind | Path pattern |
|------|----------------|
| SOC | `soc/delta2-last.json`, `soc/river2pro-last.json` |
| Watts | `watts/…-last.json` |
| Samples | `samples/read-….json` |

**Rule:** empty tree or missing file → **No data** / **Waiting**. Only measured snapshots. Never invent watts or SOC.

Vercel `/api/energy` documents this contract and returns Waiting until Hawaii publishes those files into the feed.
