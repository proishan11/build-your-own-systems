"""Learner implementation stub for Git Merge and Rebase Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_git_merge_and_rebase_lab_resolve_merges`.
"""

def plan_git_merge_and_rebase_lab_resolve_merges(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic resolve merge operations to converge observed merge graph state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
