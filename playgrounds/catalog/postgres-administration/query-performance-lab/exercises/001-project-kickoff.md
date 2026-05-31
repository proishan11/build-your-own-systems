# Exercise 001: Query Performance Lab Core Mechanism

Shared concept chapter: [postgres-admin-mental-model.md](../../../../../curriculum/concepts/postgres/postgres-admin-mental-model.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Query Performance Lab**. The work is centered on `recommend_index_query_plan`, not on a generic scaffold. You will implement behavior for **query plan** moving through **index catalog** while preserving the project invariant.

The implementation target is: Implement `recommend_index_query_plan` so Query Performance Lab has a concrete implementation boundary for query plan requests before they touch index catalog.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Query Performance Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **index catalog**. A **query plan** arrives, the component decides whether `recommend index` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `write amplification` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid query plan requests may become recommend index operations against index catalog; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `query-plan-001`, kind `recommend index`, and target `index catalog` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `recommend_index_query_plan` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `write amplification` happened in production?

## Goal

Implement `recommend_index_query_plan` so Query Performance Lab has a concrete implementation boundary for query plan requests before they touch index catalog.

## Concepts

- recovery evidence
- query plans
- replication state
- operational runbooks

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid query plan requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `write amplification` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/postgres-administration/query-performance-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- PostgreSQL backup docs: https://www.postgresql.org/docs/current/backup.html

## Staff-Level Review Questions

1. What makes this implementation specific to Query Performance Lab, rather than a generic CRUD helper?
2. Which failure mode does `write amplification` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
