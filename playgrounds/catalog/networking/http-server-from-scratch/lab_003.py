"""Learner implementation stub for HTTP Server From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_http_server_from_scratch_dispatch_handlers`.
"""

def plan_http_server_from_scratch_dispatch_handlers(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic dispatch handler operations to converge observed route table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
