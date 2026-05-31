"""Learner implementation stub for Sandboxed Coding Agent: State Model and Invariants.

Read exercises/002-state-model.md before coding. This file is
intentionally incomplete: implement the contract and use tests/test_lab_002.py
to validate behavior.
"""

class StaleEvent(Exception):
    pass


class StateModel:
    def __init__(self):
        # TODO: Track key/value state, per-key versions, seen event IDs, and audit entries.
        pass

    def apply(self, event: dict) -> dict:
        """Apply a validated event and return the current value snapshot for its key."""
        # TODO: Validate id/key/version, dedupe event IDs, reject stale versions, update state.
        raise NotImplementedError

    def get(self, key: str):
        """Return the current value for key, or None when absent."""
        # TODO: Return a safe read view without exposing internal mutable state.
        raise NotImplementedError

    def audit(self) -> list[dict]:
        """Return the ordered list of accepted events."""
        # TODO: Return a copy so callers cannot mutate internal audit history.
        raise NotImplementedError

