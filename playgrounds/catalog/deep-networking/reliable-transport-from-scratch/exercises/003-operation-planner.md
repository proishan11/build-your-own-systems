# Exercise 003: Reliable Transport From Scratch Planning and Ordering

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Reliable Transport From Scratch**. The work is centered on `plan_reliable_transport_from_scratch_ack_segments`, not on a generic scaffold. You will implement behavior for **transport segment** moving through **receive window** while preserving the project invariant.

The implementation target is: Implement `plan_reliable_transport_from_scratch_ack_segments` so Reliable Transport From Scratch can produce a deterministic ack segment plan from desired and observed receive window state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Reliable Transport From Scratch and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **receive window**. A **transport segment** arrives, the component decides whether `ack segment` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `out-of-order segment` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The same desired and observed receive window states must always produce the same minimal ordered ack segment plan.

## Tiny Example

If `receive-window-primary` is stale, `receive-window-old` is extra, and `receive-window-canary` is missing, the plan updates, deletes, then creates in stable order.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `plan_reliable_transport_from_scratch_ack_segments` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `out-of-order segment` happened in production?

## Goal

Implement `plan_reliable_transport_from_scratch_ack_segments` so Reliable Transport From Scratch can produce a deterministic ack segment plan from desired and observed receive window state.

## Concepts

- packet headers
- sequence numbers
- route selection
- loss behavior

## Files To Edit

- `lab_003.py`

## Contract

Your implementation must:

- emit update operations for changed resources
- emit delete operations for extra observed resources
- emit create operations for missing desired resources
- sort operations deterministically

## Design Hints

- Compute changed, extra, and missing sets separately.
- Sort names inside each operation group.
- Do not include no-op actions; downstream retries should be minimal.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_003.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/deep-networking/reliable-transport-from-scratch`:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9293 TCP: https://www.rfc-editor.org/rfc/rfc9293

## Staff-Level Review Questions

1. What makes this implementation specific to Reliable Transport From Scratch, rather than a generic CRUD helper?
2. Which failure mode does `out-of-order segment` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
