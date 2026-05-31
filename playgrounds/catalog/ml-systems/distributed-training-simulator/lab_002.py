"""Learner implementation stub for Distributed Training Simulator: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_distributed_training_simulator_gradient_shard_event`.
"""

def apply_distributed_training_simulator_gradient_shard_event(events: list[dict]) -> dict:
    """Apply ordered gradient shard events to worker ring while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
