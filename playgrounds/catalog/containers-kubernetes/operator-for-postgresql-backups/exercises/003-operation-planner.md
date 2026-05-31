# Exercise 003: Operator for PostgreSQL Backups Planning and Ordering

Shared concept chapter: [reconciliation-and-controllers.md](../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Operator for PostgreSQL Backups**. The work is centered on `plan_operator_for_postgresql_backups_start_backups`, not on a generic scaffold. You will implement behavior for **backup custom resource** moving through **backup schedule** while preserving the project invariant.

The implementation target is: Implement `plan_operator_for_postgresql_backups_start_backups` so Operator for PostgreSQL Backups can produce a deterministic start backup plan from desired and observed backup schedule state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Operator for PostgreSQL Backups and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **backup schedule**. A **backup custom resource** arrives, the component decides whether `start backup` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `missing wal archive` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The same desired and observed backup schedule states must always produce the same minimal ordered start backup plan.

## Tiny Example

If `backup-schedule-primary` is stale, `backup-schedule-old` is extra, and `backup-schedule-canary` is missing, the plan updates, deletes, then creates in stable order.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `plan_operator_for_postgresql_backups_start_backups` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `missing wal archive` happened in production?

## Goal

Implement `plan_operator_for_postgresql_backups_start_backups` so Operator for PostgreSQL Backups can produce a deterministic start backup plan from desired and observed backup schedule state.

## Concepts

- desired state
- observed state
- idempotent reconciliation
- isolation

## Files To Edit

- `lab_003.py`

## Contract

Your implementation must:

- emit update operations for changed resources
- emit delete operations for extra observed resources
- emit create operations for missing desired resources
- sort operations deterministically

## Design Hints

- Compute changed, extra, and missing sets separately.
- Sort names inside each operation group.
- Do not include no-op actions; downstream retries should be minimal.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_003.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/containers-kubernetes/operator-for-postgresql-backups`:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Kubernetes controller docs: https://kubernetes.io/docs/concepts/architecture/controller/

## Staff-Level Review Questions

1. What makes this implementation specific to Operator for PostgreSQL Backups, rather than a generic CRUD helper?
2. Which failure mode does `missing wal archive` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
