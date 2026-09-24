# Core Rules

## Work style

- Work quickly, but do not skip verification.
- Inspect before modifying.
- Reuse the existing architecture.
- Make the smallest change that solves the actual problem.
- Avoid unnecessary questions when the repository/source can answer the question.

## Required loop

**inspect → patch → validate → independently double-check → hand off**

## Evidence

Use:

- **Confirmed**
- **Hypothesis**
- **Unknown**
- **Historical**

Never upgrade a hypothesis to confirmed merely because it sounds plausible.

## Operator protection

The operator should not have to discover assistant mistakes.

If you make a change, verify it yourself before handing it back.

## No duplicate architecture

Do not create:

- v2 directories;
- alternate roots;
- duplicate services;
- parallel scripts;
- unnecessary installers;
- migrations;
- renamed copies of the real final file.

Use the existing final path.

## Temporary work

Disposable helpers go in `/tmp/`, not project/home directories.
