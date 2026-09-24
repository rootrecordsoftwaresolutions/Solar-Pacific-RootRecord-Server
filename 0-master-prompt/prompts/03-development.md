# Development Workflow

## Standard loop

1. Locate the actual current file.
2. Read the relevant surrounding context.
3. Trace the existing path/flow.
4. Reuse existing operations.
5. Make a surgical edit.
6. Validate syntax and behavior.
7. Independently inspect the result.
8. Hand off with exact paths and evidence.

## Drop-in discipline

Changes should land in the existing final file/path.

Do not create:

- `v2/`
- alternate roots
- renamed copies
- installers
- migration layers

unless the operator explicitly asks for them.

## Paste-safe execution

When giving commands for the operator to run:

- one paste-safe block per step;
- `set +u +o pipefail` first when using the established relay workflow;
- absolute paths;
- `cat > /absolute/path << 'EOF'` for complete file writes;
- bounded exact-match edits for surgical changes;
- backup before consequential edits;
- verify immediately afterward.

## Validation

A successful file write is not a successful feature.

Test the behavior that changed.

For a live system, verify the resulting state, not just the command's exit status.

## GitHub

Use the repository's existing GitHub structure. Do not create duplicate source copies in the Master Prompt area.

The Master Prompt area should link to frequently touched implementation files instead.

## Live-state context

Read `../state/state.json` from the master-prompt root when operational context is relevant.

Treat the snapshot as context with provenance, not as a substitute for direct verification.
