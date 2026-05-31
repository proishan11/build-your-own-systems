"""Learner implementation stub for LSM Tree KV Store: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_lsm_tree_kv_store_compact_runs`.
"""

def plan_lsm_tree_kv_store_compact_runs(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic compact run operations to converge observed sstable level state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
