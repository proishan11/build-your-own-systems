"""Learner implementation stub for Observability Stack: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_observability_stack_trace_span_event`.
"""

def apply_observability_stack_trace_span_event(events: list[dict]) -> dict:
    """Apply ordered trace span events to signal pipeline while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
