"""Learner implementation stub for Dynamic Routing Simulator: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_dynamic_routing_simulator_routing_loop`.
"""

def recover_dynamic_routing_simulator_routing_loop(failure_report: dict) -> dict:
    """Classify recovery behavior for routing loop while protecting neighbor table."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
