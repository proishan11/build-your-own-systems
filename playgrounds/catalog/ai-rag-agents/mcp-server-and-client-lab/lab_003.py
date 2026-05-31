"""Learner implementation stub for MCP Server and Client Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_mcp_server_and_client_lab_dispatch_tools`.
"""

def plan_mcp_server_and_client_lab_dispatch_tools(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic dispatch tool operations to converge observed tool registry state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
