"""Learner implementation stub for Prompt and Model Registry: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_prompt_and_model_registry_prompt_template_event`.
"""

def apply_prompt_and_model_registry_prompt_template_event(events: list[dict]) -> dict:
    """Apply ordered prompt template events to model binding while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
