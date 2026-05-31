"""Learner implementation stub for Structured Output Validator: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_structured_output_validator_model_output_event`.
"""

def apply_structured_output_validator_model_output_event(events: list[dict]) -> dict:
    """Apply ordered model output events to json schema while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
