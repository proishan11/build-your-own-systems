"""Learner implementation stub for Vim Plugin From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_vim_plugin_from_scratch_handle_autocmds`.
"""

def plan_vim_plugin_from_scratch_handle_autocmds(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic handle autocmd operations to converge observed editor state state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
