import unittest

from lab_003 import plan_feature_store_materialize_features


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_materialize_feature_operations(self):
        self.assertEqual(plan_feature_store_materialize_features({'feature-registry-primary': 'ready', 'feature-registry-canary': 'ready'}, {'feature-registry-primary': 'stale', 'feature-registry-old': 'ready'}), [{'op': 'update', 'name': 'feature-registry-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'feature-registry-old', 'from': 'ready'}, {'op': 'create', 'name': 'feature-registry-canary', 'to': 'ready'}])

    def test_noops_when_feature_registry_already_matches(self):
        current = {'feature-registry-primary': 'ready'}
        self.assertEqual(plan_feature_store_materialize_features(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_feature_store_materialize_features({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
