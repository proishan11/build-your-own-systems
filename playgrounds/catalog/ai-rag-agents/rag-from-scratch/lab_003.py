"""Learner implementation stub for RAG From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_rag_from_scratch_retrieve_contexts`.
"""

def plan_rag_from_scratch_retrieve_contexts(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic retrieve context operations to converge observed vector index state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
