import unittest

from lab_003 import plan_query_optimizer_lab_choose_plans


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_choose_plan_operations(self):
        self.assertEqual(plan_query_optimizer_lab_choose_plans({'plan-space-primary': 'ready', 'plan-space-canary': 'ready'}, {'plan-space-primary': 'stale', 'plan-space-old': 'ready'}), [{'op': 'update', 'name': 'plan-space-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'plan-space-old', 'from': 'ready'}, {'op': 'create', 'name': 'plan-space-canary', 'to': 'ready'}])

    def test_noops_when_plan_space_already_matches(self):
        current = {'plan-space-primary': 'ready'}
        self.assertEqual(plan_query_optimizer_lab_choose_plans(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_query_optimizer_lab_choose_plans({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
