"""Learner implementation stub for Layer 4 Load Balancer: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_layer_4_load_balancer_unhealthy_backend`.
"""

def recover_layer_4_load_balancer_unhealthy_backend(failure_report: dict) -> dict:
    """Classify recovery behavior for unhealthy backend while protecting backend pool."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
