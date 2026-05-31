# Exercise 005: QUIC-Like Reliable UDP Transport Integration Scenario

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **QUIC-Like Reliable UDP Transport**. The work is centered on `run_quic_like_reliable_udp_transport_scenario`, not on a generic scaffold. You will implement behavior for **quic frame** moving through **connection state** while preserving the project invariant.

The implementation target is: Implement `run_quic_like_reliable_udp_transport_scenario` so QUIC-Like Reliable UDP Transport has a deterministic integration simulation with state, `streams_open`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of QUIC-Like Reliable UDP Transport and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **connection state**. A **quic frame** arrives, the component decides whether `ack range` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `lost packet` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose connection state state and streams_open metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `connection state=ready`, recording `streams_open=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_quic_like_reliable_udp_transport_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `lost packet` happened in production?

## Goal

Implement `run_quic_like_reliable_udp_transport_scenario` so QUIC-Like Reliable UDP Transport has a deterministic integration simulation with state, `streams_open`, failures, recoveries, and invariant reporting.

## Concepts

- packet headers
- sequence numbers
- route selection
- loss behavior

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `streams_open`, failures, and recoveries
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

Run from `playgrounds/catalog/deep-networking/quic-like-reliable-udp-transport`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9293 TCP: https://www.rfc-editor.org/rfc/rfc9293

## Staff-Level Review Questions

1. What makes this implementation specific to QUIC-Like Reliable UDP Transport, rather than a generic CRUD helper?
2. Which failure mode does `lost packet` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
