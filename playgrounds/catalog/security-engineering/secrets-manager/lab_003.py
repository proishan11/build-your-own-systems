"""Learner implementation stub for Secrets Manager: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_secrets_manager_rotate_secrets`.
"""

def plan_secrets_manager_rotate_secrets(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic rotate secret operations to converge observed secret store state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
