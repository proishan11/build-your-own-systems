import unittest

from lab_004 import recover_reliable_transport_from_scratch_out_of_order_segment


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_ack_segment_failure(self):
        self.assertEqual(recover_reliable_transport_from_scratch_out_of_order_segment({'operation': 'ack segment', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'receive window'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'receive window'})

    def test_fails_permanent_out_of_order_segment(self):
        self.assertEqual(recover_reliable_transport_from_scratch_out_of_order_segment({'operation': 'ack segment', 'error': 'out-of-order segment', 'attempt': 1, 'max_attempts': 3, 'resource': 'receive window'}), {'decision': 'fail', 'reason': 'out-of-order segment', 'resource': 'receive window'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_reliable_transport_from_scratch_out_of_order_segment({'operation': 'ack segment', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'receive window'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'receive window'})


if __name__ == "__main__":
    unittest.main()
