"""Learner implementation stub for Vulnerable Web App Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_vulnerable_web_app_lab_sanitize_requests`.
"""

def plan_vulnerable_web_app_lab_sanitize_requests(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic sanitize request operations to converge observed security policy state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
