"""Learner implementation stub for Tail Latency Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_tail_latency_lab_compute_percentiles`.
"""

def plan_tail_latency_lab_compute_percentiles(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic compute percentile operations to converge observed histogram bucket state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
