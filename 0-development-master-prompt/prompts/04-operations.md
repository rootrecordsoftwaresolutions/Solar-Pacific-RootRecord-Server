# Operations

Operational work requires evidence.

## Live state

Separate:

- observed current state;
- documented policy;
- historical state;
- inferred state.

Use the labels:

**Confirmed / Hypothesis / Unknown / Historical**

## Rollback

For consequential changes:

1. exact-match check;
2. create backup;
3. edit;
4. verify;
5. retain rollback path.

## Services

Do not infer that a service is healthy merely because a unit exists.

Check the actual running process, logs, endpoint, or readback relevant to the claim.

## Scheduler/runtime

Do not treat a catalog/template as proof of active scheduling.

Verify:

- what the runtime loads;
- when it loads it;
- whether restart is required;
- whether a job actually fires;
- whether the action changes the intended state.

## Public endpoints

Do not introduce unauthenticated mutation endpoints.

Read-only/public telemetry and authenticated/mutating operations must remain distinct.

## Handoff

Every operational handoff should include:

- changed path(s);
- verification evidence;
- rollback path where relevant;
- remaining work;
- anything intentionally not tested.
