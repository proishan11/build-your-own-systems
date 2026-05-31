"""Learner implementation stub for Inference Server: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_inference_server_batch_requests`.
"""

def plan_inference_server_batch_requests(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic batch request operations to converge observed batch queue state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
