"""Learner implementation stub for Dynamic Routing Simulator: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_dynamic_routing_simulator_relax_routes`.
"""

def plan_dynamic_routing_simulator_relax_routes(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic relax route operations to converge observed neighbor table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
