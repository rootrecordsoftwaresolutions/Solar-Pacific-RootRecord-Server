# Energy / EcoFlow

The existing energy skill remains the implementation authority for EcoFlow controls.

Permanent EcoFlow action scripts belong in the established energy skill scripts location, including the per-action/per-toggle model.

Disposable EcoFlow troubleshooting scripts belong in `/tmp/`.

Do not create helper scripts in `/home/rootrecord/` merely to execute a one-off operation.

For power-flow behavior, do not infer semantics from wrapper names alone. Verify the underlying implementation and perform meaningful readback/testing before declaring behavior confirmed.

Historical policies must not be treated as current merely because they appear in an old handoff. In particular, stale statements about Delta 2 AC behavior require reconciliation against the current implementation and verified behavior.
