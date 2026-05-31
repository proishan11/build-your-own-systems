"""Learner implementation stub for OCI Image Builder: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_oci_image_builder_image_layer_event`.
"""

def apply_oci_image_builder_image_layer_event(events: list[dict]) -> dict:
    """Apply ordered image layer events to image manifest while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
