"""Learner implementation stub for LSM Tree KV Store: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_lsm_tree_kv_store_memtable_write_event`.
"""

def apply_lsm_tree_kv_store_memtable_write_event(events: list[dict]) -> dict:
    """Apply ordered memtable write events to sstable level while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
