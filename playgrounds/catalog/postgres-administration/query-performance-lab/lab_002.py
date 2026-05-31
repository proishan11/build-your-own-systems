"""Learner implementation stub for Query Performance Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_query_performance_lab_query_plan_event`.
"""

def apply_query_performance_lab_query_plan_event(events: list[dict]) -> dict:
    """Apply ordered query plan events to index catalog while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
