"""Learner implementation stub for Structured Output Validator First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class ValidationError(Exception):
    def __init__(self, errors): super().__init__('validation failed'); self.errors=errors
def validate(obj: dict, schema: dict[str,type]) -> dict:
    # TODO
    raise NotImplementedError
