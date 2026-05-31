"""Learner implementation stub for Mini Shell With Job Control: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_mini_shell_with_job_control_spawn_jobs`.
"""

def plan_mini_shell_with_job_control_spawn_jobs(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic spawn job operations to converge observed process group state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
