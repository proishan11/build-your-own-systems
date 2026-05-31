"""Learner implementation stub for Go Concurrency Gauntlet: Operation Planner and Deterministic Diffs.

Read exercises/003-operation-planner.md before coding. This file is
intentionally incomplete: implement the contract and use tests/test_lab_003.py
to validate behavior.
"""

def plan_actions(desired: dict, observed: dict) -> list[dict]:
    """Return deterministic create/update/delete actions needed to converge observed to desired."""
    # TODO: Compare desired and observed maps, sorted by key, and emit minimal actions.
    raise NotImplementedError


def summarize_plan(actions: list[dict]) -> dict:
    """Return counts by action and the total number of planned operations."""
    # TODO: Count create/update/delete operations and include total.
    raise NotImplementedError

