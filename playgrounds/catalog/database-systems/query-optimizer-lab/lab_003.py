"""Learner implementation stub for Query Optimizer Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_query_optimizer_lab_choose_plans`.
"""

def plan_query_optimizer_lab_choose_plans(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic choose plan operations to converge observed plan space state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
