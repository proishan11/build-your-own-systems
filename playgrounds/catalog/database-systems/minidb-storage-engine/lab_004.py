"""Learner implementation stub for MiniDB Storage Engine: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_minidb_storage_engine_dirty_page_loss`.
"""

def recover_minidb_storage_engine_dirty_page_loss(failure_report: dict) -> dict:
    """Classify recovery behavior for dirty page loss while protecting page cache."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
