"""Learner implementation stub for Feature Store: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_feature_store_feature_row_event`.
"""

def apply_feature_store_feature_row_event(events: list[dict]) -> dict:
    """Apply ordered feature row events to feature registry while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
