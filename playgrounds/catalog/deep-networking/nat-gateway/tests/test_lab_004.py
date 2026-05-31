import unittest

from lab_004 import recover_nat_gateway_port_exhaustion


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_allocate_port_failure(self):
        self.assertEqual(recover_nat_gateway_port_exhaustion({'operation': 'allocate port', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'translation table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'translation table'})

    def test_fails_permanent_port_exhaustion(self):
        self.assertEqual(recover_nat_gateway_port_exhaustion({'operation': 'allocate port', 'error': 'port exhaustion', 'attempt': 1, 'max_attempts': 3, 'resource': 'translation table'}), {'decision': 'fail', 'reason': 'port exhaustion', 'resource': 'translation table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_nat_gateway_port_exhaustion({'operation': 'allocate port', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'translation table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'translation table'})


if __name__ == "__main__":
    unittest.main()
