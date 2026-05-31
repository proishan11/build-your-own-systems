# Exercise 001: Query Optimizer Lab Core Mechanism

Shared concept chapter: [write-ahead-logs.md](../../../../../curriculum/concepts/storage/write-ahead-logs.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Query Optimizer Lab**. The work is centered on `choose_plan_query_predicate`, not on a generic scaffold. You will implement behavior for **query predicate** moving through **plan space** while preserving the project invariant.

The implementation target is: Implement `choose_plan_query_predicate` so Query Optimizer Lab has a concrete implementation boundary for query predicate requests before they touch plan space.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Query Optimizer Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **plan space**. A **query predicate** arrives, the component decides whether `choose plan` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `bad cardinality estimate` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid query predicate requests may become choose plan operations against plan space; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `query-predicate-001`, kind `choose plan`, and target `plan space` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `choose_plan_query_predicate` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `bad cardinality estimate` happened in production?

## Goal

Implement `choose_plan_query_predicate` so Query Optimizer Lab has a concrete implementation boundary for query predicate requests before they touch plan space.

## Concepts

- durability
- page layout
- index invariants
- recovery

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid query predicate requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `bad cardinality estimate` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/database-systems/query-optimizer-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- ARIES paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf

## Staff-Level Review Questions

1. What makes this implementation specific to Query Optimizer Lab, rather than a generic CRUD helper?
2. Which failure mode does `bad cardinality estimate` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
