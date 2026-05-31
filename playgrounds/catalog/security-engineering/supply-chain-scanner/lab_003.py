"""Learner implementation stub for Supply-Chain Scanner: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_supply_chain_scanner_scan_artifacts`.
"""

def plan_supply_chain_scanner_scan_artifacts(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic scan artifact operations to converge observed sbom index state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
