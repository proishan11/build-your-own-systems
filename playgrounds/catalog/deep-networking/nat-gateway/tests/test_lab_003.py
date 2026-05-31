import unittest

from lab_003 import plan_nat_gateway_allocate_ports


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_allocate_port_operations(self):
        self.assertEqual(plan_nat_gateway_allocate_ports({'translation-table-primary': 'ready', 'translation-table-canary': 'ready'}, {'translation-table-primary': 'stale', 'translation-table-old': 'ready'}), [{'op': 'update', 'name': 'translation-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'translation-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'translation-table-canary', 'to': 'ready'}])

    def test_noops_when_translation_table_already_matches(self):
        current = {'translation-table-primary': 'ready'}
        self.assertEqual(plan_nat_gateway_allocate_ports(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_nat_gateway_allocate_ports({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
