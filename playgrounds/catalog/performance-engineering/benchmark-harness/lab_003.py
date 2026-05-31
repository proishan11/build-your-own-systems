"""Learner implementation stub for Benchmark Harness: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_benchmark_harness_compare_runss`.
"""

def plan_benchmark_harness_compare_runss(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic compare runs operations to converge observed run config state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
