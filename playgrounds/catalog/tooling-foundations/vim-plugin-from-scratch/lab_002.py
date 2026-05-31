"""Learner implementation stub for Vim Plugin From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_vim_plugin_from_scratch_plugin_event`.
"""

def apply_vim_plugin_from_scratch_plugin_event(events: list[dict]) -> dict:
    """Apply ordered plugin events to editor state while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
