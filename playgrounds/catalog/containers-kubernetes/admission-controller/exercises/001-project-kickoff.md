# Exercise 001: Admission Controller Core Mechanism

Shared concept chapter: [reconciliation-and-controllers.md](../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Admission Controller**. The work is centered on `admit_object_admission_request`, not on a generic scaffold. You will implement behavior for **admission request** moving through **policy set** while preserving the project invariant.

The implementation target is: Implement `admit_object_admission_request` so Admission Controller has a concrete implementation boundary for admission requests before they touch policy set.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Admission Controller and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **policy set**. A **admission request** arrives, the component decides whether `admit object` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `policy bypass` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid admission requests may become admit object operations against policy set; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `admission-request-001`, kind `admit object`, and target `policy set` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `admit_object_admission_request` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `policy bypass` happened in production?

## Goal

Implement `admit_object_admission_request` so Admission Controller has a concrete implementation boundary for admission requests before they touch policy set.

## Concepts

- desired state
- observed state
- idempotent reconciliation
- isolation

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid admission requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `policy bypass` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/containers-kubernetes/admission-controller`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Kubernetes controller docs: https://kubernetes.io/docs/concepts/architecture/controller/

## Staff-Level Review Questions

1. What makes this implementation specific to Admission Controller, rather than a generic CRUD helper?
2. Which failure mode does `policy bypass` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
