# Exercise 001: Dynamic Routing Simulator Core Mechanism

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Dynamic Routing Simulator**. The work is centered on `relax_route_route_advertisement`, not on a generic scaffold. You will implement behavior for **route advertisement** moving through **neighbor table** while preserving the project invariant.

The implementation target is: Implement `relax_route_route_advertisement` so Dynamic Routing Simulator has a concrete implementation boundary for route advertisement requests before they touch neighbor table.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Dynamic Routing Simulator and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **neighbor table**. A **route advertisement** arrives, the component decides whether `relax route` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `routing loop` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid route advertisement requests may become relax route operations against neighbor table; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `route-advertisement-001`, kind `relax route`, and target `neighbor table` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `relax_route_route_advertisement` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `routing loop` happened in production?

## Goal

Implement `relax_route_route_advertisement` so Dynamic Routing Simulator has a concrete implementation boundary for route advertisement requests before they touch neighbor table.

## Concepts

- packet headers
- sequence numbers
- route selection
- loss behavior

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid route advertisement requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `routing loop` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/deep-networking/dynamic-routing-simulator`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9293 TCP: https://www.rfc-editor.org/rfc/rfc9293

## Staff-Level Review Questions

1. What makes this implementation specific to Dynamic Routing Simulator, rather than a generic CRUD helper?
2. Which failure mode does `routing loop` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
