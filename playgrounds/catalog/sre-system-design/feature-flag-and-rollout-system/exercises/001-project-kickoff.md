# Exercise 001: Feature Flag and Rollout System Core Mechanism

Shared concept chapter: [profiling-and-tail-latency.md](../../../../../curriculum/concepts/performance/profiling-and-tail-latency.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Feature Flag and Rollout System**. The work is centered on `evaluate_flag_flag_evaluation`, not on a generic scaffold. You will implement behavior for **flag evaluation** moving through **rollout rule** while preserving the project invariant.

The implementation target is: Implement `evaluate_flag_flag_evaluation` so Feature Flag and Rollout System has a concrete implementation boundary for flag evaluation requests before they touch rollout rule.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Feature Flag and Rollout System and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **rollout rule**. A **flag evaluation** arrives, the component decides whether `evaluate flag` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `bad percentage rollout` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid flag evaluation requests may become evaluate flag operations against rollout rule; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `flag-evaluation-001`, kind `evaluate flag`, and target `rollout rule` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `evaluate_flag_flag_evaluation` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `bad percentage rollout` happened in production?

## Goal

Implement `evaluate_flag_flag_evaluation` so Feature Flag and Rollout System has a concrete implementation boundary for flag evaluation requests before they touch rollout rule.

## Concepts

- service budgets
- rollouts
- observability
- overload control

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid flag evaluation requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `bad percentage rollout` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/sre-system-design/feature-flag-and-rollout-system`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- OpenTelemetry docs: https://opentelemetry.io/docs/

## Staff-Level Review Questions

1. What makes this implementation specific to Feature Flag and Rollout System, rather than a generic CRUD helper?
2. Which failure mode does `bad percentage rollout` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
