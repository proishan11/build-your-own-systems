"""Learner implementation stub for Coreutils From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_coreutils_from_scratch_transform_streams`.
"""

def plan_coreutils_from_scratch_transform_streams(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic transform stream operations to converge observed command input state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
