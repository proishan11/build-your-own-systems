"""Learner implementation stub for Feature Flag and Rollout System: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_feature_flag_and_rollout_system_evaluate_flags`.
"""

def plan_feature_flag_and_rollout_system_evaluate_flags(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic evaluate flag operations to converge observed rollout rule state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
