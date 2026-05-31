"""Learner implementation stub for Dynamic Routing Simulator: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_dynamic_routing_simulator_route_advertisement_event`.
"""

def apply_dynamic_routing_simulator_route_advertisement_event(events: list[dict]) -> dict:
    """Apply ordered route advertisement events to neighbor table while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
