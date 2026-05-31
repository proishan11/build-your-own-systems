# Exercise 001: Virtual Memory Simulator Core Mechanism

Shared concept chapter: [syscalls-traps-and-kernel-boundaries.md](../../../../../curriculum/concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Virtual Memory Simulator**. The work is centered on `map_page_virtual_page`, not on a generic scaffold. You will implement behavior for **virtual page** moving through **page table** while preserving the project invariant.

The implementation target is: Implement `map_page_virtual_page` so Virtual Memory Simulator has a concrete implementation boundary for virtual page requests before they touch page table.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Virtual Memory Simulator and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **page table**. A **virtual page** arrives, the component decides whether `map page` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `permission fault` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid virtual page requests may become map page operations against page table; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `virtual-page-001`, kind `map page`, and target `page table` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `map_page_virtual_page` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `permission fault` happened in production?

## Goal

Implement `map_page_virtual_page` so Virtual Memory Simulator has a concrete implementation boundary for virtual page requests before they touch page table.

## Concepts

- isolation
- kernel tables
- address spaces
- privileged transitions

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid virtual page requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `permission fault` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/os-kernel-labs/virtual-memory-simulator`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Berkeley CS162 notes: https://cs162.org/

## Staff-Level Review Questions

1. What makes this implementation specific to Virtual Memory Simulator, rather than a generic CRUD helper?
2. Which failure mode does `permission fault` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
