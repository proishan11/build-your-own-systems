"""Learner implementation stub for RAG From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_rag_from_scratch_document_chunk_event`.
"""

def apply_rag_from_scratch_document_chunk_event(events: list[dict]) -> dict:
    """Apply ordered document chunk events to vector index while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
