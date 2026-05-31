# Exercise 004: Vim Kata Track Failure and Recovery

Shared concept chapter: [unix-pipelines.md](../../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Vim Kata Track**. The work is centered on `recover_vim_kata_track_off_by_one_cursor`, not on a generic scaffold. You will implement behavior for **editor command** moving through **buffer state** while preserving the project invariant.

The implementation target is: Implement `recover_vim_kata_track_off_by_one_cursor` so Vim Kata Track handles transient failures, permanent `off-by-one cursor` cases, and exhausted retry budgets explicitly.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Vim Kata Track and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **buffer state**. A **editor command** arrives, the component decides whether `apply motion` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `off-by-one cursor` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Recovery decisions for buffer state must never turn a permanent off-by-one cursor into an unsafe retry.

## Tiny Example

A timeout on attempt 1 retries at attempt 2. The domain-specific failure fails immediately. A timeout at the max attempt gives up.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `recover_vim_kata_track_off_by_one_cursor` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `off-by-one cursor` happened in production?

## Goal

Implement `recover_vim_kata_track_off_by_one_cursor` so Vim Kata Track handles transient failures, permanent `off-by-one cursor` cases, and exhausted retry budgets explicitly.

## Concepts

- streams
- object identity
- repeatable workflows
- composability

## Files To Edit

- `lab_004.py`

## Contract

Your implementation must:

- retry transient timeout or unavailable errors while attempts remain
- fail permanent `off-by-one cursor` reports immediately
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

Run from `playgrounds/catalog/tooling-foundations/vim-kata-track`:

```bash
python3 -m unittest discover -s tests -p test_lab_004.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Pro Git book: https://git-scm.com/book/en/v2

## Staff-Level Review Questions

1. What makes this implementation specific to Vim Kata Track, rather than a generic CRUD helper?
2. Which failure mode does `off-by-one cursor` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
