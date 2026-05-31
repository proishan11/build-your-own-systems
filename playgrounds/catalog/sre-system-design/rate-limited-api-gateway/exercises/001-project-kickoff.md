# Exercise 001: Rate-Limited API Gateway Core Mechanism

Shared concept chapter: [profiling-and-tail-latency.md](../../../../../curriculum/concepts/performance/profiling-and-tail-latency.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Rate-Limited API Gateway**. The work is centered on `allow_request_api_request`, not on a generic scaffold. You will implement behavior for **api request** moving through **token bucket** while preserving the project invariant.

The implementation target is: Implement `allow_request_api_request` so Rate-Limited API Gateway has a concrete implementation boundary for api requests before they touch token bucket.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Rate-Limited API Gateway and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **token bucket**. A **api request** arrives, the component decides whether `allow request` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `limit bypass` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid api requests may become allow request operations against token bucket; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `api-request-001`, kind `allow request`, and target `token bucket` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `allow_request_api_request` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `limit bypass` happened in production?

## Goal

Implement `allow_request_api_request` so Rate-Limited API Gateway has a concrete implementation boundary for api requests before they touch token bucket.

## Concepts

- service budgets
- rollouts
- observability
- overload control

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid api requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `limit bypass` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/sre-system-design/rate-limited-api-gateway`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- OpenTelemetry docs: https://opentelemetry.io/docs/

## Staff-Level Review Questions

1. What makes this implementation specific to Rate-Limited API Gateway, rather than a generic CRUD helper?
2. Which failure mode does `limit bypass` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
