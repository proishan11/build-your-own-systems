import unittest

from lab_003 import plan_secrets_manager_rotate_secrets


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_rotate_secret_operations(self):
        self.assertEqual(plan_secrets_manager_rotate_secrets({'secret-store-primary': 'ready', 'secret-store-canary': 'ready'}, {'secret-store-primary': 'stale', 'secret-store-old': 'ready'}), [{'op': 'update', 'name': 'secret-store-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'secret-store-old', 'from': 'ready'}, {'op': 'create', 'name': 'secret-store-canary', 'to': 'ready'}])

    def test_noops_when_secret_store_already_matches(self):
        current = {'secret-store-primary': 'ready'}
        self.assertEqual(plan_secrets_manager_rotate_secrets(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_secrets_manager_rotate_secrets({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
