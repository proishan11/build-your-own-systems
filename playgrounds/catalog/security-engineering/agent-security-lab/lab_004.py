"""Learner implementation stub for Agent Security Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_agent_security_lab_secret_exfiltration`.
"""

def recover_agent_security_lab_secret_exfiltration(failure_report: dict) -> dict:
    """Classify recovery behavior for secret exfiltration while protecting tool policy."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
