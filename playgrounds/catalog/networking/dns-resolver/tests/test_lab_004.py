import unittest

from lab_004 import recover_dns_resolver_ttl_expiry


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_resolve_record_failure(self):
        self.assertEqual(recover_dns_resolver_ttl_expiry({'operation': 'resolve record', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'resolver cache'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'resolver cache'})

    def test_fails_permanent_ttl_expiry(self):
        self.assertEqual(recover_dns_resolver_ttl_expiry({'operation': 'resolve record', 'error': 'ttl expiry', 'attempt': 1, 'max_attempts': 3, 'resource': 'resolver cache'}), {'decision': 'fail', 'reason': 'ttl expiry', 'resource': 'resolver cache'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_dns_resolver_ttl_expiry({'operation': 'resolve record', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'resolver cache'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'resolver cache'})


if __name__ == "__main__":
    unittest.main()
