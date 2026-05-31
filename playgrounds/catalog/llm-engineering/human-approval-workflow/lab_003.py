"""Learner implementation stub for Human Approval Workflow: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_human_approval_workflow_route_approvals`.
"""

def plan_human_approval_workflow_route_approvals(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic route approval operations to converge observed approval queue state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
