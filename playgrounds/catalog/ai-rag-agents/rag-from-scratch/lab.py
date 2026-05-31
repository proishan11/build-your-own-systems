"""Learner implementation stub for RAG From Scratch First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

def chunk(doc_id: str, text: str, size: int, overlap: int) -> list[dict]:
    # TODO
    raise NotImplementedError
def retrieve(chunks: list[dict], query: str, k: int) -> list[dict]:
    # TODO
    raise NotImplementedError
