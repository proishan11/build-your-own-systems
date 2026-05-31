"""Learner implementation stub for Model Router: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_model_router_context_overflow`.
"""

def recover_model_router_context_overflow(failure_report: dict) -> dict:
    """Classify recovery behavior for context overflow while protecting model catalog."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
