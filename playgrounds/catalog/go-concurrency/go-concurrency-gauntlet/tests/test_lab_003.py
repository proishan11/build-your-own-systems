import unittest

from lab_003 import plan_go_concurrency_gauntlet_fan_out_works


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_fan_out_work_operations(self):
        self.assertEqual(plan_go_concurrency_gauntlet_fan_out_works({'worker-group-primary': 'ready', 'worker-group-canary': 'ready'}, {'worker-group-primary': 'stale', 'worker-group-old': 'ready'}), [{'op': 'update', 'name': 'worker-group-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'worker-group-old', 'from': 'ready'}, {'op': 'create', 'name': 'worker-group-canary', 'to': 'ready'}])

    def test_noops_when_worker_group_already_matches(self):
        current = {'worker-group-primary': 'ready'}
        self.assertEqual(plan_go_concurrency_gauntlet_fan_out_works(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_go_concurrency_gauntlet_fan_out_works({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
