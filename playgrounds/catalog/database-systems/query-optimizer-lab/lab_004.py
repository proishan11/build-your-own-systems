"""Learner implementation stub for Query Optimizer Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_query_optimizer_lab_bad_cardinality_estimate`.
"""

def recover_query_optimizer_lab_bad_cardinality_estimate(failure_report: dict) -> dict:
    """Classify recovery behavior for bad cardinality estimate while protecting plan space."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
