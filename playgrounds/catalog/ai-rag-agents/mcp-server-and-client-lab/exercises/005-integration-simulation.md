# Exercise 005: MCP Server and Client Lab Integration Scenario

Shared concept chapter: [rag-agents-and-tool-use.md](../../../../../curriculum/concepts/ai-agents/rag-agents-and-tool-use.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **MCP Server and Client Lab**. The work is centered on `run_mcp_server_and_client_lab_scenario`, not on a generic scaffold. You will implement behavior for **mcp request** moving through **tool registry** while preserving the project invariant.

The implementation target is: Implement `run_mcp_server_and_client_lab_scenario` so MCP Server and Client Lab has a deterministic integration simulation with state, `tool_calls_served`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of MCP Server and Client Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **tool registry**. A **mcp request** arrives, the component decides whether `dispatch tool` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `invalid json-rpc id` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose tool registry state and tool_calls_served metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `tool registry=ready`, recording `tool_calls_served=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_mcp_server_and_client_lab_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `invalid json-rpc id` happened in production?

## Goal

Implement `run_mcp_server_and_client_lab_scenario` so MCP Server and Client Lab has a deterministic integration simulation with state, `tool_calls_served`, failures, recoveries, and invariant reporting.

## Concepts

- retrieval grounding
- tool use
- provenance
- evaluation

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `tool_calls_served`, failures, and recoveries
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

Run from `playgrounds/catalog/ai-rag-agents/mcp-server-and-client-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RAG paper: https://arxiv.org/abs/2005.11401

## Staff-Level Review Questions

1. What makes this implementation specific to MCP Server and Client Lab, rather than a generic CRUD helper?
2. Which failure mode does `invalid json-rpc id` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
