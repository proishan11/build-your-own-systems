"""Learner implementation stub for GraphRAG Knowledge System: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_graphrag_knowledge_system_entity_mention_event`.
"""

def apply_graphrag_knowledge_system_entity_mention_event(events: list[dict]) -> dict:
    """Apply ordered entity mention events to knowledge graph while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
