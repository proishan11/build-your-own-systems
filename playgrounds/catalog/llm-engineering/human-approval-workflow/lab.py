"""Learner implementation stub for Human Approval Workflow First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class InvalidTransition(Exception): pass
class ApprovalWorkflow:
    def __init__(self): pass
    def request(self, action: str) -> int:
        # TODO
        raise NotImplementedError
    def approve(self, action_id: int):
        # TODO
        raise NotImplementedError
    def reject(self, action_id: int):
        # TODO
        raise NotImplementedError
    def can_execute(self, action_id: int) -> bool:
        # TODO
        raise NotImplementedError
