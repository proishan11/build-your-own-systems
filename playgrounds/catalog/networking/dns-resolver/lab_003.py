"""Learner implementation stub for DNS Resolver: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_dns_resolver_resolve_records`.
"""

def plan_dns_resolver_resolve_records(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic resolve record operations to converge observed resolver cache state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
