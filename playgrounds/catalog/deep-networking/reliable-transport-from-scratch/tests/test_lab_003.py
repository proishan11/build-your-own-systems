import unittest

from lab_003 import plan_reliable_transport_from_scratch_ack_segments


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_ack_segment_operations(self):
        self.assertEqual(plan_reliable_transport_from_scratch_ack_segments({'receive-window-primary': 'ready', 'receive-window-canary': 'ready'}, {'receive-window-primary': 'stale', 'receive-window-old': 'ready'}), [{'op': 'update', 'name': 'receive-window-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'receive-window-old', 'from': 'ready'}, {'op': 'create', 'name': 'receive-window-canary', 'to': 'ready'}])

    def test_noops_when_receive_window_already_matches(self):
        current = {'receive-window-primary': 'ready'}
        self.assertEqual(plan_reliable_transport_from_scratch_ack_segments(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_reliable_transport_from_scratch_ack_segments({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
