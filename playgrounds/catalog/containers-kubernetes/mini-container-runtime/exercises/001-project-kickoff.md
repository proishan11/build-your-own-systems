# Exercise 001: Mini Container Runtime Core Mechanism

Shared concept chapter: [reconciliation-and-controllers.md](../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Mini Container Runtime**. The work is centered on `start_container_container_spec`, not on a generic scaffold. You will implement behavior for **container spec** moving through **namespace plan** while preserving the project invariant.

The implementation target is: Implement `start_container_container_spec` so Mini Container Runtime has a concrete implementation boundary for container spec requests before they touch namespace plan.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Mini Container Runtime and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **namespace plan**. A **container spec** arrives, the component decides whether `start container` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `missing isolation` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid container spec requests may become start container operations against namespace plan; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `container-spec-001`, kind `start container`, and target `namespace plan` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `start_container_container_spec` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `missing isolation` happened in production?

## Goal

Implement `start_container_container_spec` so Mini Container Runtime has a concrete implementation boundary for container spec requests before they touch namespace plan.

## Concepts

- desired state
- observed state
- idempotent reconciliation
- isolation

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid container spec requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `missing isolation` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/containers-kubernetes/mini-container-runtime`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Kubernetes controller docs: https://kubernetes.io/docs/concepts/architecture/controller/

## Staff-Level Review Questions

1. What makes this implementation specific to Mini Container Runtime, rather than a generic CRUD helper?
2. Which failure mode does `missing isolation` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
