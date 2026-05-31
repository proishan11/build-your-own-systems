"""Learner implementation stub for Git Merge and Rebase Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_git_merge_and_rebase_lab_commit_change_event`.
"""

def apply_git_merge_and_rebase_lab_commit_change_event(events: list[dict]) -> dict:
    """Apply ordered commit change events to merge graph while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
