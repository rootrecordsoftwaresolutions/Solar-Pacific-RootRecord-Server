# Directory Tree: coms/ssh

Regenerated after dedup/merge cleanup, then moved under `coms/`: Mon Sep 21 2026

```
/home/rootrecord/.ollama/skills/coms/ssh
├── SKILL.md
├── authorized_keys
├── backups
│   ├── authorized_keys.bak
│   ├── _openssh.cpython-314.pyc.bak
│   ├── _openssh.py.bak
│   ├── _openssh.pyi.bak
│   ├── ssh.cpython-314.pyc.bak
│   └── ssh.py.bak
├── config
│   ├── ssh-relay.env
│   └── ssh-relay.env.example
├── context
│   ├── LINUX-SSH-STANDBY-2026-08-02.md
│   ├── ROOTATMUS_PRIME-Ubuntu-Server-SSH-Plan.md
│   ├── SSH-LINUX.md
│   ├── collector.js.bak-before-stable-ssh
│   └── ubuntu-server-remote-ssh-passwordless-access--c469b4a2-4ef5-4843-8535-47af457cb469.md
├── data
│   └── .gitkeep
├── logs
│   └── .gitkeep
├── run.sh
└── scripts
    ├── health-check.sh
    ├── relay-status.sh
    └── ssh-relay.sh

7 directories, 20 files
```

## Cleanup notes (this pass)

- Removed `old/` entirely — every file in it was byte-identical to a file
  already present in `context/`, `backups/`, or the top level (verified by
  md5sum/diff before deletion). Nothing was lost.
- Collapsed 4–7 numbered duplicates of the same doc (e.g.
  `ROOTATMUS_PRIME-Ubuntu-Server-SSH-Plan (2).md` through `(7).md`) down to
  one canonical copy each.
- Merged the two divergent `SKILL.md` versions (one was a purpose/philosophy
  doc, the other an operational how-to) into a single file covering both.
- Moved the single public key out of the nested `old/` folder to the skill
  root as `authorized_keys` (this is a public key — safe to keep as-is).
- `config/ssh-relay.env` was already unconfigured (all values blank) — kept
  as-is, ready for you to fill in once the new key exists.
- Dropped the stale `logs/ssh-relay.log` (single old timestamp entry) so you
  start clean on the new machine.
- No private key material was found anywhere in this archive.
