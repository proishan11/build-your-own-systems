"""Learner implementation stub for Query Performance Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_query_performance_lab_recommend_indexs`.
"""

def plan_query_performance_lab_recommend_indexs(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic recommend index operations to converge observed index catalog state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
