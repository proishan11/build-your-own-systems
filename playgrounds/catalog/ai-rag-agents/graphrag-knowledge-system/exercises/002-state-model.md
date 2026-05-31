# Exercise 002: GraphRAG Knowledge System State and Invariants

Shared concept chapter: [rag-agents-and-tool-use.md](../../../../../curriculum/concepts/ai-agents/rag-agents-and-tool-use.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **GraphRAG Knowledge System**. The work is centered on `apply_graphrag_knowledge_system_entity_mention_event`, not on a generic scaffold. You will implement behavior for **entity mention** moving through **knowledge graph** while preserving the project invariant.

The implementation target is: Implement `apply_graphrag_knowledge_system_entity_mention_event` so GraphRAG Knowledge System can replay entity mention events into knowledge graph without duplicating or accepting stale state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of GraphRAG Knowledge System and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **knowledge graph**. A **entity mention** arrives, the component decides whether `link entity` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `duplicate entity` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

knowledge graph must advance monotonically by version, and duplicate entity mention events must be idempotent.

## Tiny Example

Events `e1`, duplicate `e1`, then `e2` should accept only `e1` and `e2`. A later event with a lower version is rejected.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `apply_graphrag_knowledge_system_entity_mention_event` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `duplicate entity` happened in production?

## Goal

Implement `apply_graphrag_knowledge_system_entity_mention_event` so GraphRAG Knowledge System can replay entity mention events into knowledge graph without duplicating or accepting stale state.

## Concepts

- retrieval grounding
- tool use
- provenance
- evaluation

## Files To Edit

- `lab_002.py`

## Contract

Your implementation must:

- apply events in order
- ignore duplicate event ids
- reject stale versions
- return accepted and rejected event ids

## Design Hints

- Use a set for event ids and an integer for current version.
- Check duplicate and stale cases before updating state.
- Make the empty stream result explicit; future recovery code depends on it.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_002.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/ai-rag-agents/graphrag-knowledge-system`:

```bash
python3 -m unittest discover -s tests -p test_lab_002.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- RAG paper: https://arxiv.org/abs/2005.11401

## Staff-Level Review Questions

1. What makes this implementation specific to GraphRAG Knowledge System, rather than a generic CRUD helper?
2. Which failure mode does `duplicate entity` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
