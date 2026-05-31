"""Learner implementation stub for LLM Trace Store: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_llm_trace_store_record_spans`.
"""

def plan_llm_trace_store_record_spans(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic record span operations to converge observed trace index state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
