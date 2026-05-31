"""Learner implementation stub for Query Performance Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_query_performance_lab_write_amplification`.
"""

def recover_query_performance_lab_write_amplification(failure_report: dict) -> dict:
    """Classify recovery behavior for write amplification while protecting index catalog."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
