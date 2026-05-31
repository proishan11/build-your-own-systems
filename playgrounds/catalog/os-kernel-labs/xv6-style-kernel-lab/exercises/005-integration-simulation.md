# Exercise 005: xv6-Style Kernel Lab Integration Scenario

Shared concept chapter: [syscalls-traps-and-kernel-boundaries.md](../../../../../curriculum/concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **xv6-Style Kernel Lab**. The work is centered on `run_xv6_style_kernel_lab_scenario`, not on a generic scaffold. You will implement behavior for **system call** moving through **process table** while preserving the project invariant.

The implementation target is: Implement `run_xv6_style_kernel_lab_scenario` so xv6-Style Kernel Lab has a deterministic integration simulation with state, `syscalls_served`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of xv6-Style Kernel Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **process table**. A **system call** arrives, the component decides whether `enter kernel` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `invalid trap frame` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose process table state and syscalls_served metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `process table=ready`, recording `syscalls_served=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_xv6_style_kernel_lab_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `invalid trap frame` happened in production?

## Goal

Implement `run_xv6_style_kernel_lab_scenario` so xv6-Style Kernel Lab has a deterministic integration simulation with state, `syscalls_served`, failures, recoveries, and invariant reporting.

## Concepts

- isolation
- kernel tables
- address spaces
- privileged transitions

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `syscalls_served`, failures, and recoveries
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

Run from `playgrounds/catalog/os-kernel-labs/xv6-style-kernel-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Berkeley CS162 notes: https://cs162.org/

## Staff-Level Review Questions

1. What makes this implementation specific to xv6-Style Kernel Lab, rather than a generic CRUD helper?
2. Which failure mode does `invalid trap frame` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
