# Exercise 001: Go Concurrency Gauntlet Core Mechanism

Shared concept chapter: [pipelines-and-cancellation.md](../../../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Go Concurrency Gauntlet**. The work is centered on `fan_out_work_concurrent_job`, not on a generic scaffold. You will implement behavior for **concurrent job** moving through **worker group** while preserving the project invariant.

The implementation target is: Implement `fan_out_work_concurrent_job` so Go Concurrency Gauntlet has a concrete implementation boundary for concurrent job requests before they touch worker group.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Go Concurrency Gauntlet and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **worker group**. A **concurrent job** arrives, the component decides whether `fan out work` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `blocked sender` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid concurrent job requests may become fan out work operations against worker group; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `concurrent-job-001`, kind `fan out work`, and target `worker group` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `fan_out_work_concurrent_job` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `blocked sender` happened in production?

## Goal

Implement `fan_out_work_concurrent_job` so Go Concurrency Gauntlet has a concrete implementation boundary for concurrent job requests before they touch worker group.

## Concepts

- goroutine ownership
- cancellation
- backpressure
- deterministic shutdown

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid concurrent job requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `blocked sender` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/go-concurrency/go-concurrency-gauntlet`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Go pipelines blog: https://go.dev/blog/pipelines

## Staff-Level Review Questions

1. What makes this implementation specific to Go Concurrency Gauntlet, rather than a generic CRUD helper?
2. Which failure mode does `blocked sender` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
