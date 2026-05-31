# Exercise 001: Operator for PostgreSQL Backups Core Mechanism

Shared concept chapter: [reconciliation-and-controllers.md](../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Operator for PostgreSQL Backups**. The work is centered on `start_backup_backup_custom_resource`, not on a generic scaffold. You will implement behavior for **backup custom resource** moving through **backup schedule** while preserving the project invariant.

The implementation target is: Implement `start_backup_backup_custom_resource` so Operator for PostgreSQL Backups has a concrete implementation boundary for backup custom resource requests before they touch backup schedule.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Operator for PostgreSQL Backups and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **backup schedule**. A **backup custom resource** arrives, the component decides whether `start backup` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `missing wal archive` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid backup custom resource requests may become start backup operations against backup schedule; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `backup-custom-resource-001`, kind `start backup`, and target `backup schedule` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `start_backup_backup_custom_resource` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `missing wal archive` happened in production?

## Goal

Implement `start_backup_backup_custom_resource` so Operator for PostgreSQL Backups has a concrete implementation boundary for backup custom resource requests before they touch backup schedule.

## Concepts

- desired state
- observed state
- idempotent reconciliation
- isolation

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid backup custom resource requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `missing wal archive` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/containers-kubernetes/operator-for-postgresql-backups`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Kubernetes controller docs: https://kubernetes.io/docs/concepts/architecture/controller/

## Staff-Level Review Questions

1. What makes this implementation specific to Operator for PostgreSQL Backups, rather than a generic CRUD helper?
2. Which failure mode does `missing wal archive` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
