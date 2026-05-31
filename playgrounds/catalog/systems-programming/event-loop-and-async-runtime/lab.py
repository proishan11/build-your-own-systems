"""Learner implementation stub for Event Loop and Async Runtime First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class EventLoop:
    def __init__(self):
        self.now = 0
    def call_at(self, when: int, callback):
        # TODO: Schedule callback for logical time `when`.
        raise NotImplementedError
    def run(self):
        # TODO: Run all scheduled callbacks in deterministic order.
        raise NotImplementedError
