"""Learner implementation stub for Memory Allocator Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_memory_allocator_lab_heap_allocation_event`.
"""

def apply_memory_allocator_lab_heap_allocation_event(events: list[dict]) -> dict:
    """Apply ordered heap allocation events to free block while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
