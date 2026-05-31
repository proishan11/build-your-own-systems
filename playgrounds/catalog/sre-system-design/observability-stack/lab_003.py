"""Learner implementation stub for Observability Stack: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_observability_stack_ingest_telemetrys`.
"""

def plan_observability_stack_ingest_telemetrys(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic ingest telemetry operations to converge observed signal pipeline state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
