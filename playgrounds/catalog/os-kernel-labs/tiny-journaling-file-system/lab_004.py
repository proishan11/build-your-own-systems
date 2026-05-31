"""Learner implementation stub for Tiny Journaling File System: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_tiny_journaling_file_system_torn_journal_write`.
"""

def recover_tiny_journaling_file_system_torn_journal_write(failure_report: dict) -> dict:
    """Classify recovery behavior for torn journal write while protecting inode block."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
