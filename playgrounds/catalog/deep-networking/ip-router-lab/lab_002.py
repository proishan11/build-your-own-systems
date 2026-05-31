"""Learner implementation stub for IP Router Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_ip_router_lab_ip_packet_event`.
"""

def apply_ip_router_lab_ip_packet_event(events: list[dict]) -> dict:
    """Apply ordered ip packet events to routing table while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
