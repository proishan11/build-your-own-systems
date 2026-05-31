"""Learner implementation stub for Supply-Chain Scanner: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_supply_chain_scanner_package_artifact_event`.
"""

def apply_supply_chain_scanner_package_artifact_event(events: list[dict]) -> dict:
    """Apply ordered package artifact events to sbom index while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
