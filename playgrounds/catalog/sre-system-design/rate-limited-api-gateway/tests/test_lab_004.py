import unittest

from lab_004 import recover_rate_limited_api_gateway_limit_bypass


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_allow_request_failure(self):
        self.assertEqual(recover_rate_limited_api_gateway_limit_bypass({'operation': 'allow request', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'token bucket'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'token bucket'})

    def test_fails_permanent_limit_bypass(self):
        self.assertEqual(recover_rate_limited_api_gateway_limit_bypass({'operation': 'allow request', 'error': 'limit bypass', 'attempt': 1, 'max_attempts': 3, 'resource': 'token bucket'}), {'decision': 'fail', 'reason': 'limit bypass', 'resource': 'token bucket'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_rate_limited_api_gateway_limit_bypass({'operation': 'allow request', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'token bucket'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'token bucket'})


if __name__ == "__main__":
    unittest.main()
