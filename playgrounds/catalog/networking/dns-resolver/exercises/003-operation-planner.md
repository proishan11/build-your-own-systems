# Exercise 003: DNS Resolver Planning and Ordering

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **DNS Resolver**. The work is centered on `plan_dns_resolver_resolve_records`, not on a generic scaffold. You will implement behavior for **dns question** moving through **resolver cache** while preserving the project invariant.

The implementation target is: Implement `plan_dns_resolver_resolve_records` so DNS Resolver can produce a deterministic resolve record plan from desired and observed resolver cache state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of DNS Resolver and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **resolver cache**. A **dns question** arrives, the component decides whether `resolve record` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `ttl expiry` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The same desired and observed resolver cache states must always produce the same minimal ordered resolve record plan.

## Tiny Example

If `resolver-cache-primary` is stale, `resolver-cache-old` is extra, and `resolver-cache-canary` is missing, the plan updates, deletes, then creates in stable order.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `plan_dns_resolver_resolve_records` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `ttl expiry` happened in production?

## Goal

Implement `plan_dns_resolver_resolve_records` so DNS Resolver can produce a deterministic resolve record plan from desired and observed resolver cache state.

## Concepts

- protocol parsing
- connection state
- timeouts
- routing decisions

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

Run from `playgrounds/catalog/networking/dns-resolver`:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RFC 9112 HTTP/1.1: https://www.rfc-editor.org/rfc/rfc9112

## Staff-Level Review Questions

1. What makes this implementation specific to DNS Resolver, rather than a generic CRUD helper?
2. Which failure mode does `ttl expiry` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
