# Exercise 005: OCI Image Builder Integration Simulation and Operational Report

Shared concept chapter: [reconciliation-and-controllers.md](../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md)

## Concept Primer

This exercise deepens **OCI Image Builder** by adding the next implementation boundary after the starter lab. The focus is not broad feature count; it is building one mechanism that later project milestones can trust.

The implementation target is: Implement a small deterministic scenario runner that produces final state, metrics, invariant status, and violations.

## Why This Matters

A serious systems project becomes understandable when each layer has a contract. This exercise asks you to encode that contract in code and tests before adding more moving parts. That habit is what lets Staff engineers change complex systems without guessing.

## Mental Model

Cloud-native systems are control loops. Compare desired state with observed state, choose the smallest safe action, and make repeated execution converge rather than drift.

For this milestone, draw the component as three boxes: input, owned state, and observable output. Correct code validates the input, mutates only owned state, and returns an output that explains what happened.

## Core Invariant

The component must preserve this contract after every operation: process apply, fail, and recover events in order, return final state without exposing internal mutable structures, record processed, failed, and recovered counts. A later milestone may add scale or distribution, but it must not weaken this invariant.

## Tiny Example

Take one normal operation and one boundary operation from `tests/test_lab_005.py`. Before coding, write the expected state transition by hand. If the expected transition is hard to state in one sentence, simplify the internal representation first.

## Common Misconceptions

- Passing the first happy-path assertion means the component is finished.
- Internal state can be exposed directly because this is only a learning scaffold.
- A retry, replay, duplicate, or malformed input can be handled later without shaping the API now.
- Do not write a controller action that only works the first time it runs.

## Self-Check

Before coding, answer:

1. What state does this exercise introduce that exercise 001 did not need?
2. Which branch protects the invariant before mutation?
3. What behavior must remain deterministic for review and debugging?
4. What would you measure or log when this component misbehaves?

## Goal

Implement a small deterministic scenario runner that produces final state, metrics, invariant status, and violations.

## Concepts

- reconciliation
- desired vs observed state
- idempotency
- runtime isolation

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, fail, and recover events in order
- return final state without exposing internal mutable structures
- record processed, failed, and recovered counts
- mark invariant violations for malformed events instead of crashing silently

## Design Hints

- Keep the representation boring and explicit; clever encodings hide invariants.
- Implement validation and idempotency before optimizing the successful path.
- Prefer deterministic ordering for every returned list, report, or plan.
- Make boundary behavior visible in the return value or exception type.

## Layered Hints

### Hint 1

Start with the data structure that makes the invariant obvious. Most of the code should become simple conditionals over that structure.

### Hint 2

Run the test file directly and implement one assertion at a time. Do not start by trying to satisfy every scenario at once.

### Hint 3

After the tests pass, look for accidental mutation leaks: returned dictionaries and lists should not let callers corrupt internal state.

## Validation

Run from `playgrounds/catalog/containers-kubernetes/oci-image-builder`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Reconciliation and controllers: ../../../../../curriculum/concepts/containers-kubernetes/reconciliation-and-controllers.md
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/

## Staff-Level Review Questions

1. What invariant did this milestone add or strengthen?
2. Which malformed, duplicate, stale, or partial input should be tested next?
3. How would this implementation behave under replay or retry?
4. What would make this component easier to debug in production?
