import unittest

from lab_003 import plan_vim_plugin_from_scratch_handle_autocmds


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_handle_autocmd_operations(self):
        self.assertEqual(plan_vim_plugin_from_scratch_handle_autocmds({'editor-state-primary': 'ready', 'editor-state-canary': 'ready'}, {'editor-state-primary': 'stale', 'editor-state-old': 'ready'}), [{'op': 'update', 'name': 'editor-state-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'editor-state-old', 'from': 'ready'}, {'op': 'create', 'name': 'editor-state-canary', 'to': 'ready'}])

    def test_noops_when_editor_state_already_matches(self):
        current = {'editor-state-primary': 'ready'}
        self.assertEqual(plan_vim_plugin_from_scratch_handle_autocmds(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_vim_plugin_from_scratch_handle_autocmds({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
