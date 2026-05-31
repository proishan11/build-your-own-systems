"""Learner implementation stub for Tiny Journaling File System: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_tiny_journaling_file_system_commit_records`.
"""

def plan_tiny_journaling_file_system_commit_records(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic commit record operations to converge observed inode block state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
