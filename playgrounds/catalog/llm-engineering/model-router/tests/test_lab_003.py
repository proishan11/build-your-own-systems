import unittest

from lab_003 import plan_model_router_route_models


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_route_model_operations(self):
        self.assertEqual(plan_model_router_route_models({'model-catalog-primary': 'ready', 'model-catalog-canary': 'ready'}, {'model-catalog-primary': 'stale', 'model-catalog-old': 'ready'}), [{'op': 'update', 'name': 'model-catalog-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'model-catalog-old', 'from': 'ready'}, {'op': 'create', 'name': 'model-catalog-canary', 'to': 'ready'}])

    def test_noops_when_model_catalog_already_matches(self):
        current = {'model-catalog-primary': 'ready'}
        self.assertEqual(plan_model_router_route_models(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_model_router_route_models({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
