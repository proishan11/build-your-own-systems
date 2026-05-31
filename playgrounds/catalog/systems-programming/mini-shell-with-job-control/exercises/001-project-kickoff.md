# Exercise 001: Mini Shell With Job Control Core Mechanism

Shared concept chapter: [unix-pipelines.md](../../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Mini Shell With Job Control**. The work is centered on `spawn_job_command_pipeline`, not on a generic scaffold. You will implement behavior for **command pipeline** moving through **process group** while preserving the project invariant.

The implementation target is: Implement `spawn_job_command_pipeline` so Mini Shell With Job Control has a concrete implementation boundary for command pipeline requests before they touch process group.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Mini Shell With Job Control and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **process group**. A **command pipeline** arrives, the component decides whether `spawn job` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `orphaned background job` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid command pipeline requests may become spawn job operations against process group; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `command-pipeline-001`, kind `spawn job`, and target `process group` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `spawn_job_command_pipeline` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `orphaned background job` happened in production?

## Goal

Implement `spawn_job_command_pipeline` so Mini Shell With Job Control has a concrete implementation boundary for command pipeline requests before they touch process group.

## Concepts

- resource ownership
- process state
- explicit cleanup
- error boundaries

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid command pipeline requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `orphaned background job` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/systems-programming/mini-shell-with-job-control`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- xv6 book and source: https://pdos.csail.mit.edu/6.828/2019/xv6.html

## Staff-Level Review Questions

1. What makes this implementation specific to Mini Shell With Job Control, rather than a generic CRUD helper?
2. Which failure mode does `orphaned background job` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
