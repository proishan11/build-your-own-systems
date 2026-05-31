"""Learner implementation stub for HTTP Server From Scratch First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

from dataclasses import dataclass
class BadRequest(Exception): pass
@dataclass(frozen=True)
class Request: method: str; path: str; version: str; headers: dict[str,str]
def parse_request(raw: str) -> Request:
    # TODO: Parse request line and headers.
    raise NotImplementedError
