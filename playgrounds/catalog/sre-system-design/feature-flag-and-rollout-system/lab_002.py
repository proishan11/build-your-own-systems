"""Learner implementation stub for Feature Flag and Rollout System: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_feature_flag_and_rollout_system_flag_evaluation_event`.
"""

def apply_feature_flag_and_rollout_system_flag_evaluation_event(events: list[dict]) -> dict:
    """Apply ordered flag evaluation events to rollout rule while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
