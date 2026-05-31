import unittest

from lab_003 import plan_ip_router_lab_forward_packets


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_forward_packet_operations(self):
        self.assertEqual(plan_ip_router_lab_forward_packets({'routing-table-primary': 'ready', 'routing-table-canary': 'ready'}, {'routing-table-primary': 'stale', 'routing-table-old': 'ready'}), [{'op': 'update', 'name': 'routing-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'routing-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'routing-table-canary', 'to': 'ready'}])

    def test_noops_when_routing_table_already_matches(self):
        current = {'routing-table-primary': 'ready'}
        self.assertEqual(plan_ip_router_lab_forward_packets(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_ip_router_lab_forward_packets({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
