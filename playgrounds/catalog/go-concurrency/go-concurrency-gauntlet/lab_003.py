"""Learner implementation stub for Go Concurrency Gauntlet: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_go_concurrency_gauntlet_fan_out_works`.
"""

def plan_go_concurrency_gauntlet_fan_out_works(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic fan out work operations to converge observed worker group state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
