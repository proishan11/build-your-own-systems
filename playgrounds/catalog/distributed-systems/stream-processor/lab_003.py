"""Learner implementation stub for Stream Processor: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_stream_processor_advance_watermarks`.
"""

def plan_stream_processor_advance_watermarks(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic advance watermark operations to converge observed watermark state state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
