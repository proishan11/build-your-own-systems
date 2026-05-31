"""Learner implementation stub for Auth and Session System: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_auth_and_session_system_authenticate_sessions`.
"""

def plan_auth_and_session_system_authenticate_sessions(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic authenticate session operations to converge observed session store state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
