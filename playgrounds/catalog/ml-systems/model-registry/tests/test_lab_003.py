import unittest

from lab_003 import plan_model_registry_promote_models


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_promote_model_operations(self):
        self.assertEqual(plan_model_registry_promote_models({'registry-version-primary': 'ready', 'registry-version-canary': 'ready'}, {'registry-version-primary': 'stale', 'registry-version-old': 'ready'}), [{'op': 'update', 'name': 'registry-version-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'registry-version-old', 'from': 'ready'}, {'op': 'create', 'name': 'registry-version-canary', 'to': 'ready'}])

    def test_noops_when_registry_version_already_matches(self):
        current = {'registry-version-primary': 'ready'}
        self.assertEqual(plan_model_registry_promote_models(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_model_registry_promote_models({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
