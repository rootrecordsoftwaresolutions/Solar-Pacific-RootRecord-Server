# Repository & Frequently Touched File Links

This file is the navigation index for major RootRecord files that are repeatedly inspected or modified.

**Rule:** these are links to the real source files. Do not copy those files into the Master Prompt repository.

## Solar Pacific RootRecord Server

Repository:
https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server

### Development / operating context

- `0-development-master-prompt/` — operator's development master-prompt area (the current handoff ZIP contains the authoritative workflow material used to update this index)
- `Workflow-Rules.md` — paste-safe execution, evidence, backup, relay, and verification conventions
- `00_READ_FIRST.md` — entry-point/read-first context

> Note: the GitHub API view available during this update did not expose the `0-development-master-prompt` path on the default branch, so the two links above are intentionally represented as directory/file navigation targets rather than claimed as currently verified API paths. The uploaded 2026-09-24 handoff is the source used for their content.

### Energy

- [`energy/lib/ble_client.py`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/blob/main/energy/lib/ble_client.py)
- [`energy/`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/tree/main/energy)
- [`automations/scripts/jobs.py`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/blob/main/automations/scripts/jobs.py)

### Operational structure

- [`automations/`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/tree/main/automations)
- [`coms/`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/tree/main/coms)
- [`agents/`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/tree/main/agents)
- [`status/`](https://github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server/tree/main/status)

## US Mainland Server

Repository:
https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server

### Network globe

The current GitHub mirror search identified:

- [`mirror/network-globe/server.js`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/mirror/network-globe/server.js)
- [`mirror/network-globe/HAWAII-MERGE.md`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/mirror/network-globe/HAWAII-MERGE.md)
- [`mirror/network-globe/start.sh`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/mirror/network-globe/start.sh)
- [`mirror/network-globe/package.json`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/mirror/network-globe/package.json)
- [`mirror/network-globe/README.md`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/mirror/network-globe/README.md)
- [`RECOVERY.md`](https://github.com/rootrecordsoftwaresolutions/US-Mainland-Server/blob/main/RECOVERY.md)

Important: the repository is a mirror/recovery representation. Verify the deployed AWS path before treating a GitHub mirror file as live runtime state.

## RootRecord Website

Repository:
https://github.com/rootrecordsoftwaresolutions/RootRecord-Website

Frequently touched current files identified from the repository:

- [`README.md`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/README.md)
- [`src/app/home/page.tsx`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/src/app/home/page.tsx)
- [`src/app/api/energy/route.ts`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/src/app/api/energy/route.ts)
- [`src/components/SiteChrome.tsx`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/src/components/SiteChrome.tsx)
- [`src/components/EnergyBoard.tsx`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/src/components/EnergyBoard.tsx)
- [`src/app/globals.css`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Website/blob/main/src/app/globals.css)

## RootRecord Master Prompt

- [`MASTER-PROMPT.md`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt/blob/main/MASTER-PROMPT.md)
- [`README.md`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt/blob/main/README.md)
- [`prompts/`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt/tree/main/prompts)
- [`manifest/prompts.yaml`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt/blob/main/manifest/prompts.yaml)
- [`skill/SKILL.md`](https://github.com/rootrecordsoftwaresolutions/RootRecord-Master-Prompt/blob/main/skill/SKILL.md)

## Link maintenance rule

When a frequently touched file changes location:

1. update this index;
2. do not create a duplicate copy just to preserve an old link;
3. if the old path is historically important, label it **Historical** and point to the new canonical file;
4. do not claim a link is live/deployed merely because it exists in GitHub.
