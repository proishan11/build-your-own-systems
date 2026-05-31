"""Learner implementation stub for NAT Gateway: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_nat_gateway_allocate_ports`.
"""

def plan_nat_gateway_allocate_ports(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic allocate port operations to converge observed translation table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
