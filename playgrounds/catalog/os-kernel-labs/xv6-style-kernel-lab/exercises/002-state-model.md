# Exercise 002: xv6-Style Kernel Lab State and Invariants

Shared concept chapter: [syscalls-traps-and-kernel-boundaries.md](../../../../../curriculum/concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **xv6-Style Kernel Lab**. The work is centered on `apply_xv6_style_kernel_lab_system_call_event`, not on a generic scaffold. You will implement behavior for **system call** moving through **process table** while preserving the project invariant.

The implementation target is: Implement `apply_xv6_style_kernel_lab_system_call_event` so xv6-Style Kernel Lab can replay system call events into process table without duplicating or accepting stale state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of xv6-Style Kernel Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **process table**. A **system call** arrives, the component decides whether `enter kernel` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `invalid trap frame` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

process table must advance monotonically by version, and duplicate system call events must be idempotent.

## Tiny Example

Events `e1`, duplicate `e1`, then `e2` should accept only `e1` and `e2`. A later event with a lower version is rejected.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `apply_xv6_style_kernel_lab_system_call_event` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `invalid trap frame` happened in production?

## Goal

Implement `apply_xv6_style_kernel_lab_system_call_event` so xv6-Style Kernel Lab can replay system call events into process table without duplicating or accepting stale state.

## Concepts

- isolation
- kernel tables
- address spaces
- privileged transitions

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

Run from `playgrounds/catalog/os-kernel-labs/xv6-style-kernel-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_002.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Berkeley CS162 notes: https://cs162.org/

## Staff-Level Review Questions

1. What makes this implementation specific to xv6-Style Kernel Lab, rather than a generic CRUD helper?
2. Which failure mode does `invalid trap frame` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
