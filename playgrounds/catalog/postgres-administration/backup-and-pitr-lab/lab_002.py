"""Learner implementation stub for Backup and PITR Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_backup_and_pitr_lab_wal_segment_event`.
"""

def apply_backup_and_pitr_lab_wal_segment_event(events: list[dict]) -> dict:
    """Apply ordered wal segment events to backup catalog while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
