"""Learner implementation stub for Layer 4 Load Balancer: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_layer_4_load_balancer_choose_backends`.
"""

def plan_layer_4_load_balancer_choose_backends(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic choose backend operations to converge observed backend pool state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
