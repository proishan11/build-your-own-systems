# Exercise 001: Dynamo-Style KV Store Core Mechanism

Shared concept chapter: [raft-and-replicated-logs.md](../../../../../curriculum/concepts/distributed-systems/raft-and-replicated-logs.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Dynamo-Style KV Store**. The work is centered on `write_quorum_kv_write`, not on a generic scaffold. You will implement behavior for **kv write** moving through **replica set** while preserving the project invariant.

The implementation target is: Implement `write_quorum_kv_write` so Dynamo-Style KV Store has a concrete implementation boundary for kv write requests before they touch replica set.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Dynamo-Style KV Store and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **replica set**. A **kv write** arrives, the component decides whether `write quorum` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `sibling conflict` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid kv write requests may become write quorum operations against replica set; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `kv-write-001`, kind `write quorum`, and target `replica set` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `write_quorum_kv_write` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `sibling conflict` happened in production?

## Goal

Implement `write_quorum_kv_write` so Dynamo-Style KV Store has a concrete implementation boundary for kv write requests before they touch replica set.

## Concepts

- replication
- quorums
- idempotency
- partial failure

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid kv write requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `sibling conflict` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/distributed-systems/dynamo-style-kv-store`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Raft paper: https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro

## Staff-Level Review Questions

1. What makes this implementation specific to Dynamo-Style KV Store, rather than a generic CRUD helper?
2. Which failure mode does `sibling conflict` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
