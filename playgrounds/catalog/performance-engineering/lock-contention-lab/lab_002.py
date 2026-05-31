"""Learner implementation stub for Lock Contention Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_lock_contention_lab_lock_event`.
"""

def apply_lock_contention_lab_lock_event(events: list[dict]) -> dict:
    """Apply ordered lock events to wait graph while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
