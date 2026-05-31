import unittest

from lab_003 import plan_mini_deep_learning_framework_run_forward_passs


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_run_forward_pass_operations(self):
        self.assertEqual(plan_mini_deep_learning_framework_run_forward_passs({'module-graph-primary': 'ready', 'module-graph-canary': 'ready'}, {'module-graph-primary': 'stale', 'module-graph-old': 'ready'}), [{'op': 'update', 'name': 'module-graph-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'module-graph-old', 'from': 'ready'}, {'op': 'create', 'name': 'module-graph-canary', 'to': 'ready'}])

    def test_noops_when_module_graph_already_matches(self):
        current = {'module-graph-primary': 'ready'}
        self.assertEqual(plan_mini_deep_learning_framework_run_forward_passs(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mini_deep_learning_framework_run_forward_passs({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
