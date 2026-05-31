"""Learner implementation stub for Observability Stack: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_observability_stack_cardinality_explosion`.
"""

def recover_observability_stack_cardinality_explosion(failure_report: dict) -> dict:
    """Classify recovery behavior for cardinality explosion while protecting signal pipeline."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
