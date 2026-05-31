import unittest

from lab_004 import recover_vulnerable_web_app_lab_xss_payload


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_sanitize_request_failure(self):
        self.assertEqual(recover_vulnerable_web_app_lab_xss_payload({'operation': 'sanitize request', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'security policy'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'security policy'})

    def test_fails_permanent_xss_payload(self):
        self.assertEqual(recover_vulnerable_web_app_lab_xss_payload({'operation': 'sanitize request', 'error': 'xss payload', 'attempt': 1, 'max_attempts': 3, 'resource': 'security policy'}), {'decision': 'fail', 'reason': 'xss payload', 'resource': 'security policy'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_vulnerable_web_app_lab_xss_payload({'operation': 'sanitize request', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'security policy'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'security policy'})


if __name__ == "__main__":
    unittest.main()
