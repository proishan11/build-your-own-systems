"""Learner implementation stub for Scheduler Simulator: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_scheduler_simulator_bind_pods`.
"""

def plan_scheduler_simulator_bind_pods(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic bind pod operations to converge observed node inventory state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
