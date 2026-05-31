"""Learner implementation stub for Agent Security Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

READ_ONLY = {"read_file", "search", "list_issues"}
MUTATING = {"write_file", "create_pr", "restart_service"}
DENIED = {"exfiltrate_secret", "disable_audit_log", "rm_rf"}


def classify_tool_call(tool: str, args: dict) -> tuple[str, str]:
    """Return (decision, reason) for an agent tool call.

    decision is one of: "allow", "approval", "deny".
    """
    # TODO: Implement explicit classification and include a useful reason.
    raise NotImplementedError
