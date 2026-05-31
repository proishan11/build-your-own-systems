"""Learner implementation stub for Rate-Limited API Gateway: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_rate_limited_api_gateway_allow_requests`.
"""

def plan_rate_limited_api_gateway_allow_requests(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic allow request operations to converge observed token bucket state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
