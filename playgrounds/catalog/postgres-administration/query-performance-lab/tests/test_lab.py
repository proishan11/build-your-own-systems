import unittest

from lab import recommend_index_query_plan


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_query_plan_request(self):
        self.assertEqual(recommend_index_query_plan({'id': 'query-plan-001', 'kind': 'recommend index', 'target': 'index catalog', 'priority': 2, 'metadata': {'source': 'Query Performance Lab', 'track': 'postgres-administration'}}), {'id': 'query-plan-001', 'action': 'recommend index', 'target': 'index catalog', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_query_plan_request(self):
        self.assertEqual(recommend_index_query_plan({'id': 'bad', 'kind': '', 'target': 'index catalog', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'index catalog', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'query-plan-001', 'kind': 'recommend index', 'target': 'index catalog', 'priority': 2, 'metadata': {'source': 'Query Performance Lab', 'track': 'postgres-administration'}}
        original = dict(request)
        recommend_index_query_plan(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
