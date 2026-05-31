"""Learner implementation stub for Backup and PITR Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_backup_and_pitr_lab_restore_targets`.
"""

def plan_backup_and_pitr_lab_restore_targets(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic restore target operations to converge observed backup catalog state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
