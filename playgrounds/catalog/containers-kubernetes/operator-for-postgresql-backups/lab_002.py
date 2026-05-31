"""Learner implementation stub for Operator for PostgreSQL Backups: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_operator_for_postgresql_backups_backup_custom_resource_event`.
"""

def apply_operator_for_postgresql_backups_backup_custom_resource_event(events: list[dict]) -> dict:
    """Apply ordered backup custom resource events to backup schedule while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
