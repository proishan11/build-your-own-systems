"""Learner implementation stub for xv6-Style Kernel Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class PageFault(Exception): pass
class AddressSpace:
    def __init__(self, page_size: int = 4096):
        self.page_size = page_size
    def map(self, vpn: int, frame: int, *, read=True, write=False):
        # TODO: Store mapping and permissions.
        raise NotImplementedError
    def translate(self, va: int, *, write=False) -> int:
        # TODO: Return physical address or raise PageFault.
        raise NotImplementedError
