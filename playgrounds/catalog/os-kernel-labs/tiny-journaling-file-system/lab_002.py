"""Learner implementation stub for Tiny Journaling File System: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_tiny_journaling_file_system_journal_transaction_event`.
"""

def apply_tiny_journaling_file_system_journal_transaction_event(events: list[dict]) -> dict:
    """Apply ordered journal transaction events to inode block while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
