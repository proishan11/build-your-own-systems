"""Learner implementation stub for Kubernetes Controller From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_kubernetes_controller_from_scratch_custom_resource_event`.
"""

def apply_kubernetes_controller_from_scratch_custom_resource_event(events: list[dict]) -> dict:
    """Apply ordered custom resource events to reconcile state while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
