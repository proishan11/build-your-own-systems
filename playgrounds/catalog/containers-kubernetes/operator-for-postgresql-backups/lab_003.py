"""Learner implementation stub for Operator for PostgreSQL Backups: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_operator_for_postgresql_backups_start_backups`.
"""

def plan_operator_for_postgresql_backups_start_backups(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic start backup operations to converge observed backup schedule state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
