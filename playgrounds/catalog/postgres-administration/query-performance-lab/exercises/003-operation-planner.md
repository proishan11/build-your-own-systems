# Exercise 003: Query Performance Lab Planning and Ordering

Shared concept chapter: [postgres-admin-mental-model.md](../../../../../curriculum/concepts/postgres/postgres-admin-mental-model.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Query Performance Lab**. The work is centered on `plan_query_performance_lab_recommend_indexs`, not on a generic scaffold. You will implement behavior for **query plan** moving through **index catalog** while preserving the project invariant.

The implementation target is: Implement `plan_query_performance_lab_recommend_indexs` so Query Performance Lab can produce a deterministic recommend index plan from desired and observed index catalog state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Query Performance Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **index catalog**. A **query plan** arrives, the component decides whether `recommend index` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `write amplification` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The same desired and observed index catalog states must always produce the same minimal ordered recommend index plan.

## Tiny Example

If `index-catalog-primary` is stale, `index-catalog-old` is extra, and `index-catalog-canary` is missing, the plan updates, deletes, then creates in stable order.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `plan_query_performance_lab_recommend_indexs` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `write amplification` happened in production?

## Goal

Implement `plan_query_performance_lab_recommend_indexs` so Query Performance Lab can produce a deterministic recommend index plan from desired and observed index catalog state.

## Concepts

- recovery evidence
- query plans
- replication state
- operational runbooks

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

Run from `playgrounds/catalog/postgres-administration/query-performance-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- PostgreSQL backup docs: https://www.postgresql.org/docs/current/backup.html

## Staff-Level Review Questions

1. What makes this implementation specific to Query Performance Lab, rather than a generic CRUD helper?
2. Which failure mode does `write amplification` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
