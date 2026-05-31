import unittest

from lab import choose_plan_query_predicate


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_query_predicate_request(self):
        self.assertEqual(choose_plan_query_predicate({'id': 'query-predicate-001', 'kind': 'choose plan', 'target': 'plan space', 'priority': 2, 'metadata': {'source': 'Query Optimizer Lab', 'track': 'database-systems'}}), {'id': 'query-predicate-001', 'action': 'choose plan', 'target': 'plan space', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_query_predicate_request(self):
        self.assertEqual(choose_plan_query_predicate({'id': 'bad', 'kind': '', 'target': 'plan space', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'plan space', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'query-predicate-001', 'kind': 'choose plan', 'target': 'plan space', 'priority': 2, 'metadata': {'source': 'Query Optimizer Lab', 'track': 'database-systems'}}
        original = dict(request)
        choose_plan_query_predicate(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
