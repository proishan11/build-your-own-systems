"""Learner implementation stub for QUIC-Like Reliable UDP Transport: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_quic_like_reliable_udp_transport_ack_ranges`.
"""

def plan_quic_like_reliable_udp_transport_ack_ranges(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic ack range operations to converge observed connection state state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
