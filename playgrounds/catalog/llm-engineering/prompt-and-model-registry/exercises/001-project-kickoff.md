# Exercise 001: Prompt and Model Registry Core Mechanism

Shared concept chapter: [llm-evals-traces-and-guardrails.md](../../../../../curriculum/concepts/llm-engineering/llm-evals-traces-and-guardrails.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Prompt and Model Registry**. The work is centered on `publish_prompt_prompt_template`, not on a generic scaffold. You will implement behavior for **prompt template** moving through **model binding** while preserving the project invariant.

The implementation target is: Implement `publish_prompt_prompt_template` so Prompt and Model Registry has a concrete implementation boundary for prompt template requests before they touch model binding.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Prompt and Model Registry and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **model binding**. A **prompt template** arrives, the component decides whether `publish prompt` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `unsafe prompt change` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid prompt template requests may become publish prompt operations against model binding; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `prompt-template-001`, kind `publish prompt`, and target `model binding` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `publish_prompt_prompt_template` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `unsafe prompt change` happened in production?

## Goal

Implement `publish_prompt_prompt_template` so Prompt and Model Registry has a concrete implementation boundary for prompt template requests before they touch model binding.

## Concepts

- prompt contracts
- traceability
- guardrails
- cost and latency

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid prompt template requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `unsafe prompt change` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/llm-engineering/prompt-and-model-registry`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest

## Staff-Level Review Questions

1. What makes this implementation specific to Prompt and Model Registry, rather than a generic CRUD helper?
2. Which failure mode does `unsafe prompt change` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
