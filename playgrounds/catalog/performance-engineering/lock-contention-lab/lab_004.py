"""Learner implementation stub for Lock Contention Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_lock_contention_lab_convoy_effect`.
"""

def recover_lock_contention_lab_convoy_effect(failure_report: dict) -> dict:
    """Classify recovery behavior for convoy effect while protecting wait graph."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
