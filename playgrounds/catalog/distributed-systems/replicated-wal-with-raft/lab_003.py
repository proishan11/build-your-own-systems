"""Learner implementation stub for Replicated WAL With Raft: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_replicated_wal_with_raft_append_entriess`.
"""

def plan_replicated_wal_with_raft_append_entriess(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic append entries operations to converge observed replica log state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
