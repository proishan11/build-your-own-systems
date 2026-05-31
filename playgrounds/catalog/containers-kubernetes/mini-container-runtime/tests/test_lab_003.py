import unittest

from lab_003 import plan_mini_container_runtime_start_containers


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_start_container_operations(self):
        self.assertEqual(plan_mini_container_runtime_start_containers({'namespace-plan-primary': 'ready', 'namespace-plan-canary': 'ready'}, {'namespace-plan-primary': 'stale', 'namespace-plan-old': 'ready'}), [{'op': 'update', 'name': 'namespace-plan-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'namespace-plan-old', 'from': 'ready'}, {'op': 'create', 'name': 'namespace-plan-canary', 'to': 'ready'}])

    def test_noops_when_namespace_plan_already_matches(self):
        current = {'namespace-plan-primary': 'ready'}
        self.assertEqual(plan_mini_container_runtime_start_containers(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mini_container_runtime_start_containers({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
