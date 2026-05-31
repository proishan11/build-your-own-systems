"""Learner implementation stub for Observability With eBPF Concepts: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_observability_with_ebpf_concepts_kernel_event`.
"""

def apply_observability_with_ebpf_concepts_kernel_event(events: list[dict]) -> dict:
    """Apply ordered kernel events to probe registry while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
