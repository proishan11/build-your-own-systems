"""Learner implementation stub for IP Router Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_ip_router_lab_forward_packets`.
"""

def plan_ip_router_lab_forward_packets(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic forward packet operations to converge observed routing table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
