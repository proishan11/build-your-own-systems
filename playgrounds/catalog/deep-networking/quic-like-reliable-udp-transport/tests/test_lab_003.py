import unittest

from lab_003 import plan_quic_like_reliable_udp_transport_ack_ranges


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_ack_range_operations(self):
        self.assertEqual(plan_quic_like_reliable_udp_transport_ack_ranges({'connection-state-primary': 'ready', 'connection-state-canary': 'ready'}, {'connection-state-primary': 'stale', 'connection-state-old': 'ready'}), [{'op': 'update', 'name': 'connection-state-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'connection-state-old', 'from': 'ready'}, {'op': 'create', 'name': 'connection-state-canary', 'to': 'ready'}])

    def test_noops_when_connection_state_already_matches(self):
        current = {'connection-state-primary': 'ready'}
        self.assertEqual(plan_quic_like_reliable_udp_transport_ack_ranges(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_quic_like_reliable_udp_transport_ack_ranges({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
