import unittest

from lab_003 import plan_stream_processor_advance_watermarks


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_advance_watermark_operations(self):
        self.assertEqual(plan_stream_processor_advance_watermarks({'watermark-state-primary': 'ready', 'watermark-state-canary': 'ready'}, {'watermark-state-primary': 'stale', 'watermark-state-old': 'ready'}), [{'op': 'update', 'name': 'watermark-state-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'watermark-state-old', 'from': 'ready'}, {'op': 'create', 'name': 'watermark-state-canary', 'to': 'ready'}])

    def test_noops_when_watermark_state_already_matches(self):
        current = {'watermark-state-primary': 'ready'}
        self.assertEqual(plan_stream_processor_advance_watermarks(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_stream_processor_advance_watermarks({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
