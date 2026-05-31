"""Learner implementation stub for NAT Gateway: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_nat_gateway_outbound_flow_event`.
"""

def apply_nat_gateway_outbound_flow_event(events: list[dict]) -> dict:
    """Apply ordered outbound flow events to translation table while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
