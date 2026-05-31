"""Learner implementation stub for Lock Contention Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_lock_contention_lab_attribute_waits`.
"""

def plan_lock_contention_lab_attribute_waits(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic attribute wait operations to converge observed wait graph state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
