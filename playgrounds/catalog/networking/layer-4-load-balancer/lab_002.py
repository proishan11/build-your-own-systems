"""Learner implementation stub for Layer 4 Load Balancer: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_layer_4_load_balancer_tcp_flow_event`.
"""

def apply_layer_4_load_balancer_tcp_flow_event(events: list[dict]) -> dict:
    """Apply ordered tcp flow events to backend pool while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
