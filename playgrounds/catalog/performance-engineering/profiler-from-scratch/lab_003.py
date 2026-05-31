"""Learner implementation stub for Profiler From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_profiler_from_scratch_aggregate_samples`.
"""

def plan_profiler_from_scratch_aggregate_samples(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic aggregate sample operations to converge observed profile tree state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
