# Exercise 001: MCP Server and Client Lab Core Mechanism

Shared concept chapter: [rag-agents-and-tool-use.md](../../../../../curriculum/concepts/ai-agents/rag-agents-and-tool-use.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **MCP Server and Client Lab**. The work is centered on `dispatch_tool_mcp_request`, not on a generic scaffold. You will implement behavior for **mcp request** moving through **tool registry** while preserving the project invariant.

The implementation target is: Implement `dispatch_tool_mcp_request` so MCP Server and Client Lab has a concrete implementation boundary for mcp requests before they touch tool registry.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of MCP Server and Client Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **tool registry**. A **mcp request** arrives, the component decides whether `dispatch tool` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `invalid json-rpc id` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Only valid mcp requests may become dispatch tool operations against tool registry; malformed input must produce a deterministic rejection.

## Tiny Example

A valid request with id `mcp-request-001`, kind `dispatch tool`, and target `tool registry` becomes a concrete operation. A request with an empty kind is rejected before it can mutate state.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `dispatch_tool_mcp_request` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `invalid json-rpc id` happened in production?

## Goal

Implement `dispatch_tool_mcp_request` so MCP Server and Client Lab has a concrete implementation boundary for mcp requests before they touch tool registry.

## Concepts

- retrieval grounding
- tool use
- provenance
- evaluation

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- build valid mcp requests into a stable project operation
- preserve id, target, and priority
- reject malformed requests with a stable reason
- avoid mutating caller-owned input

## Design Hints

- Name the validation checks before building the output dictionary.
- Treat `invalid json-rpc id` as the kind of bad input that must never reach mutation code.
- Return plain dictionaries so the tests can inspect the domain decision directly.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/ai-rag-agents/mcp-server-and-client-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RAG paper: https://arxiv.org/abs/2005.11401

## Staff-Level Review Questions

1. What makes this implementation specific to MCP Server and Client Lab, rather than a generic CRUD helper?
2. Which failure mode does `invalid json-rpc id` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
