import unittest

from lab_003 import plan_layer_4_load_balancer_choose_backends


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_choose_backend_operations(self):
        self.assertEqual(plan_layer_4_load_balancer_choose_backends({'backend-pool-primary': 'ready', 'backend-pool-canary': 'ready'}, {'backend-pool-primary': 'stale', 'backend-pool-old': 'ready'}), [{'op': 'update', 'name': 'backend-pool-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'backend-pool-old', 'from': 'ready'}, {'op': 'create', 'name': 'backend-pool-canary', 'to': 'ready'}])

    def test_noops_when_backend_pool_already_matches(self):
        current = {'backend-pool-primary': 'ready'}
        self.assertEqual(plan_layer_4_load_balancer_choose_backends(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_layer_4_load_balancer_choose_backends({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
