"""Learner implementation stub for MCP Server and Client Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class ToolError(Exception): pass
class ToolRegistry:
    def __init__(self): pass
    def register(self, name: str, required: set[str]):
        # TODO
        raise NotImplementedError
    def call(self, name: str, args: dict) -> dict:
        # TODO: Validate and return call record.
        raise NotImplementedError
    def calls(self) -> list[dict]:
        # TODO
        raise NotImplementedError
