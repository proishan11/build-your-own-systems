import unittest

from lab_003 import plan_scheduler_simulator_bind_pods


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_bind_pod_operations(self):
        self.assertEqual(plan_scheduler_simulator_bind_pods({'node-inventory-primary': 'ready', 'node-inventory-canary': 'ready'}, {'node-inventory-primary': 'stale', 'node-inventory-old': 'ready'}), [{'op': 'update', 'name': 'node-inventory-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'node-inventory-old', 'from': 'ready'}, {'op': 'create', 'name': 'node-inventory-canary', 'to': 'ready'}])

    def test_noops_when_node_inventory_already_matches(self):
        current = {'node-inventory-primary': 'ready'}
        self.assertEqual(plan_scheduler_simulator_bind_pods(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_scheduler_simulator_bind_pods({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
