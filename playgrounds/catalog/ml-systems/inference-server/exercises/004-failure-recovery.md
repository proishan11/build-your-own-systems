# Exercise 004: Inference Server Failure and Recovery

Shared concept chapter: [autograd-and-training-loops.md](../../../../../curriculum/concepts/ml-systems/autograd-and-training-loops.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Inference Server**. The work is centered on `recover_inference_server_deadline_miss`, not on a generic scaffold. You will implement behavior for **inference request** moving through **batch queue** while preserving the project invariant.

The implementation target is: Implement `recover_inference_server_deadline_miss` so Inference Server handles transient failures, permanent `deadline miss` cases, and exhausted retry budgets explicitly.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Inference Server and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **batch queue**. A **inference request** arrives, the component decides whether `batch request` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `deadline miss` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Recovery decisions for batch queue must never turn a permanent deadline miss into an unsafe retry.

## Tiny Example

A timeout on attempt 1 retries at attempt 2. The domain-specific failure fails immediately. A timeout at the max attempt gives up.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `recover_inference_server_deadline_miss` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `deadline miss` happened in production?

## Goal

Implement `recover_inference_server_deadline_miss` so Inference Server handles transient failures, permanent `deadline miss` cases, and exhausted retry budgets explicitly.

## Concepts

- data lineage
- shape contracts
- serving constraints
- reproducibility

## Files To Edit

- `lab_004.py`

## Contract

Your implementation must:

- retry transient timeout or unavailable errors while attempts remain
- fail permanent `deadline miss` reports immediately
- give up when retry budget is exhausted
- include resource and reason fields for operators

## Design Hints

- Classify permanent domain failures before retryable infrastructure failures.
- Compare `attempt` to `max_attempts` before returning retry.
- Return structured decisions; strings alone are too hard to operate.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_004.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/ml-systems/inference-server`:

```bash
python3 -m unittest discover -s tests -p test_lab_004.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- CMU ML in Production: https://mlip-cmu.github.io/

## Staff-Level Review Questions

1. What makes this implementation specific to Inference Server, rather than a generic CRUD helper?
2. Which failure mode does `deadline miss` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
