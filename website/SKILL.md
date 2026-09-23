---
name: website
description: >-
  RootRecord public site (Next.js foundation) → RootRecord-Website via mirror
  sync every 300s. Edit site/ here; baks under Database/GITHUB/.
---

# website

| | |
|--|--|
| Edit | `site/` (Next.js App Router) |
| GitHub | `rootrecordsoftwaresolutions/RootRecord-Website` |
| Sync | poller `github_sync_all` (mirror → Database/GITHUB/worktrees/website) |
| Baks | `/home/rootrecord/Database/GITHUB/` |
| Intake | `/home/rootrecord/Database/intake/` |

Foundation only — no heavy API until rebuild continues.
