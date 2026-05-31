"""Learner implementation stub for MiniDB Storage Engine: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_minidb_storage_engine_database_record_event`.
"""

def apply_minidb_storage_engine_database_record_event(events: list[dict]) -> dict:
    """Apply ordered database record events to page cache while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
