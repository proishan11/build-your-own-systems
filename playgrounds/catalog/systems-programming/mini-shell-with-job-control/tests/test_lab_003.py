import unittest

from lab_003 import plan_mini_shell_with_job_control_spawn_jobs


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_spawn_job_operations(self):
        self.assertEqual(plan_mini_shell_with_job_control_spawn_jobs({'process-group-primary': 'ready', 'process-group-canary': 'ready'}, {'process-group-primary': 'stale', 'process-group-old': 'ready'}), [{'op': 'update', 'name': 'process-group-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'process-group-old', 'from': 'ready'}, {'op': 'create', 'name': 'process-group-canary', 'to': 'ready'}])

    def test_noops_when_process_group_already_matches(self):
        current = {'process-group-primary': 'ready'}
        self.assertEqual(plan_mini_shell_with_job_control_spawn_jobs(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mini_shell_with_job_control_spawn_jobs({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
