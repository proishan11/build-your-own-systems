"""Learner implementation stub for Model Router: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_model_router_route_models`.
"""

def plan_model_router_route_models(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic route model operations to converge observed model catalog state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
