"""Learner implementation stub for NAT Gateway: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_nat_gateway_port_exhaustion`.
"""

def recover_nat_gateway_port_exhaustion(failure_report: dict) -> dict:
    """Classify recovery behavior for port exhaustion while protecting translation table."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
