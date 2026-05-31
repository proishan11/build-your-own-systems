import unittest

from lab_003 import plan_mapreduce_runtime_schedule_tasks


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_schedule_task_operations(self):
        self.assertEqual(plan_mapreduce_runtime_schedule_tasks({'task-tracker-primary': 'ready', 'task-tracker-canary': 'ready'}, {'task-tracker-primary': 'stale', 'task-tracker-old': 'ready'}), [{'op': 'update', 'name': 'task-tracker-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'task-tracker-old', 'from': 'ready'}, {'op': 'create', 'name': 'task-tracker-canary', 'to': 'ready'}])

    def test_noops_when_task_tracker_already_matches(self):
        current = {'task-tracker-primary': 'ready'}
        self.assertEqual(plan_mapreduce_runtime_schedule_tasks(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mapreduce_runtime_schedule_tasks({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
