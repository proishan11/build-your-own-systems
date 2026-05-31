import unittest

from lab_003 import plan_event_loop_and_async_runtime_schedule_callbacks


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_schedule_callback_operations(self):
        self.assertEqual(plan_event_loop_and_async_runtime_schedule_callbacks({'ready-queue-primary': 'ready', 'ready-queue-canary': 'ready'}, {'ready-queue-primary': 'stale', 'ready-queue-old': 'ready'}), [{'op': 'update', 'name': 'ready-queue-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'ready-queue-old', 'from': 'ready'}, {'op': 'create', 'name': 'ready-queue-canary', 'to': 'ready'}])

    def test_noops_when_ready_queue_already_matches(self):
        current = {'ready-queue-primary': 'ready'}
        self.assertEqual(plan_event_loop_and_async_runtime_schedule_callbacks(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_event_loop_and_async_runtime_schedule_callbacks({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
