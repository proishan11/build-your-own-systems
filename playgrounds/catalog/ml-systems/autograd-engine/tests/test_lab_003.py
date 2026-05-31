import unittest

from lab_003 import plan_autograd_engine_backpropagate_gradients


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_backpropagate_gradient_operations(self):
        self.assertEqual(plan_autograd_engine_backpropagate_gradients({'computation-graph-primary': 'ready', 'computation-graph-canary': 'ready'}, {'computation-graph-primary': 'stale', 'computation-graph-old': 'ready'}), [{'op': 'update', 'name': 'computation-graph-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'computation-graph-old', 'from': 'ready'}, {'op': 'create', 'name': 'computation-graph-canary', 'to': 'ready'}])

    def test_noops_when_computation_graph_already_matches(self):
        current = {'computation-graph-primary': 'ready'}
        self.assertEqual(plan_autograd_engine_backpropagate_gradients(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_autograd_engine_backpropagate_gradients({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
