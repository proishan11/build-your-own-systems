"""Learner implementation stub for Reliable Transport From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_reliable_transport_from_scratch_ack_segments`.
"""

def plan_reliable_transport_from_scratch_ack_segments(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic ack segment operations to converge observed receive window state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
