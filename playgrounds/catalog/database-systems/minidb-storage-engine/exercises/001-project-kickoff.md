# Exercise 001: MiniDB Storage Engine Core Mechanism

Shared concept chapter: [write-ahead-logs.md](../../../../../curriculum/concepts/storage/write-ahead-logs.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **MiniDB Storage Engine**. The work is centered on `write_record_database_record`, not on a generic scaffold. You will implement behavior for **database record** moving through **page cache** while preserving the project invariant.

The implementation target is: Implement `write_record_database_record` so MiniDB Storage Engine has a concrete implementation boundary for database record requests before they touch page cache.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of MiniDB Storage Engine and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **page cache**. A **database record** arrives, the component decides whether `write record` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `dirty page loss` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid database record requests may become write record operations against page cache; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `database-record-001`, kind `write record`, and target `page cache` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `write_record_database_record` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `dirty page loss` happened in production?

## Goal

Implement `write_record_database_record` so MiniDB Storage Engine has a concrete implementation boundary for database record requests before they touch page cache.

## Concepts

- durability
- page layout
- index invariants
- recovery

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid database record requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `dirty page loss` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/database-systems/minidb-storage-engine`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- ARIES paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf

## Staff-Level Review Questions

1. What makes this implementation specific to MiniDB Storage Engine, rather than a generic CRUD helper?
2. Which failure mode does `dirty page loss` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
