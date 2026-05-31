"""Learner implementation stub for Model Registry: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_model_registry_model_artifact_event`.
"""

def apply_model_registry_model_artifact_event(events: list[dict]) -> dict:
    """Apply ordered model artifact events to registry version while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
