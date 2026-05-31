# Exercise 001: Layer 4 Load Balancer Core Mechanism

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Layer 4 Load Balancer**. The work is centered on `choose_backend_tcp_flow`, not on a generic scaffold. You will implement behavior for **tcp flow** moving through **backend pool** while preserving the project invariant.

The implementation target is: Implement `choose_backend_tcp_flow` so Layer 4 Load Balancer has a concrete implementation boundary for tcp flow requests before they touch backend pool.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Layer 4 Load Balancer and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **backend pool**. A **tcp flow** arrives, the component decides whether `choose backend` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `unhealthy backend` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid tcp flow requests may become choose backend operations against backend pool; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `tcp-flow-001`, kind `choose backend`, and target `backend pool` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `choose_backend_tcp_flow` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `unhealthy backend` happened in production?

## Goal

Implement `choose_backend_tcp_flow` so Layer 4 Load Balancer has a concrete implementation boundary for tcp flow requests before they touch backend pool.

## Concepts

- protocol parsing
- connection state
- timeouts
- routing decisions

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid tcp flow requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `unhealthy backend` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/networking/layer-4-load-balancer`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9112 HTTP/1.1: https://www.rfc-editor.org/rfc/rfc9112

## Staff-Level Review Questions

1. What makes this implementation specific to Layer 4 Load Balancer, rather than a generic CRUD helper?
2. Which failure mode does `unhealthy backend` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
