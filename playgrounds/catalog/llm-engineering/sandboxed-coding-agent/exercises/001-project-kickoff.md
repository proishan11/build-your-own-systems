# Exercise 001: Sandboxed Coding Agent Core Mechanism

Shared concept chapter: [llm-evals-traces-and-guardrails.md](../../../../../curriculum/concepts/llm-engineering/llm-evals-traces-and-guardrails.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Sandboxed Coding Agent**. The work is centered on `authorize_tool_tool_invocation`, not on a generic scaffold. You will implement behavior for **tool invocation** moving through **sandbox policy** while preserving the project invariant.

The implementation target is: Implement `authorize_tool_tool_invocation` so Sandboxed Coding Agent has a concrete implementation boundary for tool invocation requests before they touch sandbox policy.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Sandboxed Coding Agent and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **sandbox policy**. A **tool invocation** arrives, the component decides whether `authorize tool` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `filesystem escape` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid tool invocation requests may become authorize tool operations against sandbox policy; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `tool-invocation-001`, kind `authorize tool`, and target `sandbox policy` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `authorize_tool_tool_invocation` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `filesystem escape` happened in production?

## Goal

Implement `authorize_tool_tool_invocation` so Sandboxed Coding Agent has a concrete implementation boundary for tool invocation requests before they touch sandbox policy.

## Concepts

- prompt contracts
- traceability
- guardrails
- cost and latency

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid tool invocation requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `filesystem escape` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/llm-engineering/sandboxed-coding-agent`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest

## Staff-Level Review Questions

1. What makes this implementation specific to Sandboxed Coding Agent, rather than a generic CRUD helper?
2. Which failure mode does `filesystem escape` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
