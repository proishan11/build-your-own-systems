"""Learner implementation stub for Autograd Engine First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class Value:
    def __init__(self, data: float): self.data=data; self.grad=0.0
    def __add__(self, other):
        # TODO
        raise NotImplementedError
    def __mul__(self, other):
        # TODO
        raise NotImplementedError
    def backward(self):
        # TODO
        raise NotImplementedError
