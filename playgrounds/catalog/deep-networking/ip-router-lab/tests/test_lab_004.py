import unittest

from lab_004 import recover_ip_router_lab_ttl_expired


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_forward_packet_failure(self):
        self.assertEqual(recover_ip_router_lab_ttl_expired({'operation': 'forward packet', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'routing table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'routing table'})

    def test_fails_permanent_ttl_expired(self):
        self.assertEqual(recover_ip_router_lab_ttl_expired({'operation': 'forward packet', 'error': 'ttl expired', 'attempt': 1, 'max_attempts': 3, 'resource': 'routing table'}), {'decision': 'fail', 'reason': 'ttl expired', 'resource': 'routing table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_ip_router_lab_ttl_expired({'operation': 'forward packet', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'routing table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'routing table'})


if __name__ == "__main__":
    unittest.main()
