"""Learner implementation stub for Cost and Latency Dashboard: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_cost_and_latency_dashboard_tail_spike`.
"""

def recover_cost_and_latency_dashboard_tail_spike(failure_report: dict) -> dict:
    """Classify recovery behavior for tail spike while protecting metric bucket."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
