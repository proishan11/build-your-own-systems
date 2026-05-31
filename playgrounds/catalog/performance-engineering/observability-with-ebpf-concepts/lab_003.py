"""Learner implementation stub for Observability With eBPF Concepts: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_observability_with_ebpf_concepts_attach_probes`.
"""

def plan_observability_with_ebpf_concepts_attach_probes(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic attach probe operations to converge observed probe registry state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
