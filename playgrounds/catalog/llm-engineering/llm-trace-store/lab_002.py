"""Learner implementation stub for LLM Trace Store: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_llm_trace_store_llm_span_event`.
"""

def apply_llm_trace_store_llm_span_event(events: list[dict]) -> dict:
    """Apply ordered llm span events to trace index while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
