"""Learner implementation stub for Supply-Chain Scanner: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_supply_chain_scanner_unsigned_dependency`.
"""

def recover_supply_chain_scanner_unsigned_dependency(failure_report: dict) -> dict:
    """Classify recovery behavior for unsigned dependency while protecting sbom index."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
