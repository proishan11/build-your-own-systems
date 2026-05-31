import unittest

from lab_003 import plan_dynamic_routing_simulator_relax_routes


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_relax_route_operations(self):
        self.assertEqual(plan_dynamic_routing_simulator_relax_routes({'neighbor-table-primary': 'ready', 'neighbor-table-canary': 'ready'}, {'neighbor-table-primary': 'stale', 'neighbor-table-old': 'ready'}), [{'op': 'update', 'name': 'neighbor-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'neighbor-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'neighbor-table-canary', 'to': 'ready'}])

    def test_noops_when_neighbor_table_already_matches(self):
        current = {'neighbor-table-primary': 'ready'}
        self.assertEqual(plan_dynamic_routing_simulator_relax_routes(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_dynamic_routing_simulator_relax_routes({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
