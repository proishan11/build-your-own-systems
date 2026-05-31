"""Learner implementation stub for MCP Server and Client Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_mcp_server_and_client_lab_mcp_request_event`.
"""

def apply_mcp_server_and_client_lab_mcp_request_event(events: list[dict]) -> dict:
    """Apply ordered mcp request events to tool registry while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
