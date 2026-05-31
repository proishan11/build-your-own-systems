"""Learner implementation stub for Mini Shell With Job Control First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

import shlex

class ParseError(Exception):
    pass

def parse_pipeline(command_line: str) -> list[list[str]]:
    """Parse a simple pipeline into argv lists."""
    # TODO: Use shlex with punctuation support or equivalent parsing.
    raise NotImplementedError
