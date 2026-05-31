# Exercise 005: Backup and PITR Lab Integration Scenario

Shared concept chapter: [postgres-admin-mental-model.md](../../../../../curriculum/concepts/postgres/postgres-admin-mental-model.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Backup and PITR Lab**. The work is centered on `run_backup_and_pitr_lab_scenario`, not on a generic scaffold. You will implement behavior for **wal segment** moving through **backup catalog** while preserving the project invariant.

The implementation target is: Implement `run_backup_and_pitr_lab_scenario` so Backup and PITR Lab has a deterministic integration simulation with state, `segments_restored`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Backup and PITR Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **backup catalog**. A **wal segment** arrives, the component decides whether `restore target` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `missing base backup` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose backup catalog state and segments_restored metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `backup catalog=ready`, recording `segments_restored=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_backup_and_pitr_lab_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `missing base backup` happened in production?

## Goal

Implement `run_backup_and_pitr_lab_scenario` so Backup and PITR Lab has a deterministic integration simulation with state, `segments_restored`, failures, recoveries, and invariant reporting.

## Concepts

- recovery evidence
- query plans
- replication state
- operational runbooks

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `segments_restored`, failures, and recoveries
- return invariant_ok and violations
- handle empty scenarios deterministically

## Design Hints

- Initialize the full report shape before processing events.
- Treat missing resources as violations, not exceptions.
- Keep metric defaults explicit so dashboards do not infer missing data.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_005.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/postgres-administration/backup-and-pitr-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- PostgreSQL backup docs: https://www.postgresql.org/docs/current/backup.html

## Staff-Level Review Questions

1. What makes this implementation specific to Backup and PITR Lab, rather than a generic CRUD helper?
2. Which failure mode does `missing base backup` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
