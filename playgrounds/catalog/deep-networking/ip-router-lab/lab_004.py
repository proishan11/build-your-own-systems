"""Learner implementation stub for IP Router Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_ip_router_lab_ttl_expired`.
"""

def recover_ip_router_lab_ttl_expired(failure_report: dict) -> dict:
    """Classify recovery behavior for ttl expired while protecting routing table."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
