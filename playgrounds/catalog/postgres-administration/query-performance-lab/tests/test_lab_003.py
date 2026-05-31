import unittest

from lab_003 import plan_query_performance_lab_recommend_indexs


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_recommend_index_operations(self):
        self.assertEqual(plan_query_performance_lab_recommend_indexs({'index-catalog-primary': 'ready', 'index-catalog-canary': 'ready'}, {'index-catalog-primary': 'stale', 'index-catalog-old': 'ready'}), [{'op': 'update', 'name': 'index-catalog-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'index-catalog-old', 'from': 'ready'}, {'op': 'create', 'name': 'index-catalog-canary', 'to': 'ready'}])

    def test_noops_when_index_catalog_already_matches(self):
        current = {'index-catalog-primary': 'ready'}
        self.assertEqual(plan_query_performance_lab_recommend_indexs(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_query_performance_lab_recommend_indexs({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
