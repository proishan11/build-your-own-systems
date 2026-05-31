"""Learner implementation stub for GraphRAG Knowledge System: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_graphrag_knowledge_system_link_entitys`.
"""

def plan_graphrag_knowledge_system_link_entitys(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic link entity operations to converge observed knowledge graph state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
