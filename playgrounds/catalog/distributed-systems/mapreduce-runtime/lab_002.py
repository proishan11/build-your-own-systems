"""Learner implementation stub for MapReduce Runtime: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_mapreduce_runtime_map_task_event`.
"""

def apply_mapreduce_runtime_map_task_event(events: list[dict]) -> dict:
    """Apply ordered map task events to task tracker while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
