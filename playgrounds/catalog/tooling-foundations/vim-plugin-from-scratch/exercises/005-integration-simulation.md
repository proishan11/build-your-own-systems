# Exercise 005: Vim Plugin From Scratch Integration Scenario

Shared concept chapter: [unix-pipelines.md](../../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Vim Plugin From Scratch**. The work is centered on `run_vim_plugin_from_scratch_scenario`, not on a generic scaffold. You will implement behavior for **plugin event** moving through **editor state** while preserving the project invariant.

The implementation target is: Implement `run_vim_plugin_from_scratch_scenario` so Vim Plugin From Scratch has a deterministic integration simulation with state, `events_handled`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Vim Plugin From Scratch and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **editor state**. A **plugin event** arrives, the component decides whether `handle autocmd` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `recursive mapping` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose editor state state and events_handled metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `editor state=ready`, recording `events_handled=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_vim_plugin_from_scratch_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `recursive mapping` happened in production?

## Goal

Implement `run_vim_plugin_from_scratch_scenario` so Vim Plugin From Scratch has a deterministic integration simulation with state, `events_handled`, failures, recoveries, and invariant reporting.

## Concepts

- streams
- object identity
- repeatable workflows
- composability

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `events_handled`, failures, and recoveries
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

Run from `playgrounds/catalog/tooling-foundations/vim-plugin-from-scratch`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Pro Git book: https://git-scm.com/book/en/v2

## Staff-Level Review Questions

1. What makes this implementation specific to Vim Plugin From Scratch, rather than a generic CRUD helper?
2. Which failure mode does `recursive mapping` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
