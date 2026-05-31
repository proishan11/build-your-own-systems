# Exercise 002: IP Router Lab State and Invariants

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **IP Router Lab**. The work is centered on `apply_ip_router_lab_ip_packet_event`, not on a generic scaffold. You will implement behavior for **ip packet** moving through **routing table** while preserving the project invariant.

The implementation target is: Implement `apply_ip_router_lab_ip_packet_event` so IP Router Lab can replay ip packet events into routing table without duplicating or accepting stale state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of IP Router Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **routing table**. A **ip packet** arrives, the component decides whether `forward packet` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `ttl expired` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

routing table must advance monotonically by version, and duplicate ip packet events must be idempotent.

## Tiny Example

Events `e1`, duplicate `e1`, then `e2` should accept only `e1` and `e2`. A later event with a lower version is rejected.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `apply_ip_router_lab_ip_packet_event` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `ttl expired` happened in production?

## Goal

Implement `apply_ip_router_lab_ip_packet_event` so IP Router Lab can replay ip packet events into routing table without duplicating or accepting stale state.

## Concepts

- packet headers
- sequence numbers
- route selection
- loss behavior

## Files To Edit

- `lab_002.py`

## Contract

Your implementation must:

- apply events in order
- ignore duplicate event ids
- reject stale versions
- return accepted and rejected event ids

## Design Hints

- Use a set for event ids and an integer for current version.
- Check duplicate and stale cases before updating state.
- Make the empty stream result explicit; future recovery code depends on it.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_002.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/deep-networking/ip-router-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_002.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9293 TCP: https://www.rfc-editor.org/rfc/rfc9293

## Staff-Level Review Questions

1. What makes this implementation specific to IP Router Lab, rather than a generic CRUD helper?
2. Which failure mode does `ttl expired` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
