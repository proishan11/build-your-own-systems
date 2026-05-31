# Exercise 005: Query Optimizer Lab Integration Scenario

Shared concept chapter: [write-ahead-logs.md](../../../../../curriculum/concepts/storage/write-ahead-logs.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Query Optimizer Lab**. The work is centered on `run_query_optimizer_lab_scenario`, not on a generic scaffold. You will implement behavior for **query predicate** moving through **plan space** while preserving the project invariant.

The implementation target is: Implement `run_query_optimizer_lab_scenario` so Query Optimizer Lab has a deterministic integration simulation with state, `estimated_cost`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Query Optimizer Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **plan space**. A **query predicate** arrives, the component decides whether `choose plan` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `bad cardinality estimate` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose plan space state and estimated_cost metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `plan space=ready`, recording `estimated_cost=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_query_optimizer_lab_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `bad cardinality estimate` happened in production?

## Goal

Implement `run_query_optimizer_lab_scenario` so Query Optimizer Lab has a deterministic integration simulation with state, `estimated_cost`, failures, recoveries, and invariant reporting.

## Concepts

- durability
- page layout
- index invariants
- recovery

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `estimated_cost`, failures, and recoveries
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

Run from `playgrounds/catalog/database-systems/query-optimizer-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- ARIES paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf

## Staff-Level Review Questions

1. What makes this implementation specific to Query Optimizer Lab, rather than a generic CRUD helper?
2. Which failure mode does `bad cardinality estimate` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
