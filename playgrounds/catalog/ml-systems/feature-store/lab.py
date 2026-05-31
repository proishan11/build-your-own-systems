"""Learner implementation stub for Feature Store First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class FeatureStore:
    def __init__(self): pass
    def put(self, entity: str, feature: str, timestamp: int, value):
        # TODO
        raise NotImplementedError
    def get_as_of(self, entity: str, feature: str, timestamp: int):
        # TODO
        raise NotImplementedError
