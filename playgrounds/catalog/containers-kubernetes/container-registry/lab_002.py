"""Learner implementation stub for Container Registry: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_container_registry_image_blob_event`.
"""

def apply_container_registry_image_blob_event(events: list[dict]) -> dict:
    """Apply ordered image blob events to blob store while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
