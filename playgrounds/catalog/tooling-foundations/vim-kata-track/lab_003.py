"""Learner implementation stub for Vim Kata Track: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_vim_kata_track_apply_motions`.
"""

def plan_vim_kata_track_apply_motions(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic apply motion operations to converge observed buffer state state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
