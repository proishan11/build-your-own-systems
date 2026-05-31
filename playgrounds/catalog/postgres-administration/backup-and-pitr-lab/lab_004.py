"""Learner implementation stub for Backup and PITR Lab: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_backup_and_pitr_lab_missing_base_backup`.
"""

def recover_backup_and_pitr_lab_missing_base_backup(failure_report: dict) -> dict:
    """Classify recovery behavior for missing base backup while protecting backup catalog."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
