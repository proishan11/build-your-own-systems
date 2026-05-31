import unittest

from lab_003 import plan_user_level_thread_library_yield_threads


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_yield_thread_operations(self):
        self.assertEqual(plan_user_level_thread_library_yield_threads({'run-queue-primary': 'ready', 'run-queue-canary': 'ready'}, {'run-queue-primary': 'stale', 'run-queue-old': 'ready'}), [{'op': 'update', 'name': 'run-queue-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'run-queue-old', 'from': 'ready'}, {'op': 'create', 'name': 'run-queue-canary', 'to': 'ready'}])

    def test_noops_when_run_queue_already_matches(self):
        current = {'run-queue-primary': 'ready'}
        self.assertEqual(plan_user_level_thread_library_yield_threads(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_user_level_thread_library_yield_threads({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
