import unittest

from lab_003 import plan_virtual_memory_simulator_map_pages


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_map_page_operations(self):
        self.assertEqual(plan_virtual_memory_simulator_map_pages({'page-table-primary': 'ready', 'page-table-canary': 'ready'}, {'page-table-primary': 'stale', 'page-table-old': 'ready'}), [{'op': 'update', 'name': 'page-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'page-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'page-table-canary', 'to': 'ready'}])

    def test_noops_when_page_table_already_matches(self):
        current = {'page-table-primary': 'ready'}
        self.assertEqual(plan_virtual_memory_simulator_map_pages(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_virtual_memory_simulator_map_pages({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
