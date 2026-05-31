import unittest

from lab_003 import plan_rate_limited_api_gateway_allow_requests


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_allow_request_operations(self):
        self.assertEqual(plan_rate_limited_api_gateway_allow_requests({'token-bucket-primary': 'ready', 'token-bucket-canary': 'ready'}, {'token-bucket-primary': 'stale', 'token-bucket-old': 'ready'}), [{'op': 'update', 'name': 'token-bucket-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'token-bucket-old', 'from': 'ready'}, {'op': 'create', 'name': 'token-bucket-canary', 'to': 'ready'}])

    def test_noops_when_token_bucket_already_matches(self):
        current = {'token-bucket-primary': 'ready'}
        self.assertEqual(plan_rate_limited_api_gateway_allow_requests(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_rate_limited_api_gateway_allow_requests({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
