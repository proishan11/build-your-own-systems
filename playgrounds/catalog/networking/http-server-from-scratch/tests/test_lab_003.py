import unittest

from lab_003 import plan_http_server_from_scratch_dispatch_handlers


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_dispatch_handler_operations(self):
        self.assertEqual(plan_http_server_from_scratch_dispatch_handlers({'route-table-primary': 'ready', 'route-table-canary': 'ready'}, {'route-table-primary': 'stale', 'route-table-old': 'ready'}), [{'op': 'update', 'name': 'route-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'route-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'route-table-canary', 'to': 'ready'}])

    def test_noops_when_route_table_already_matches(self):
        current = {'route-table-primary': 'ready'}
        self.assertEqual(plan_http_server_from_scratch_dispatch_handlers(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_http_server_from_scratch_dispatch_handlers({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
