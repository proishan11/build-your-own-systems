"""Learner implementation stub for Replicated WAL With Raft: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_replicated_wal_with_raft_term_mismatch`.
"""

def recover_replicated_wal_with_raft_term_mismatch(failure_report: dict) -> dict:
    """Classify recovery behavior for term mismatch while protecting replica log."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
