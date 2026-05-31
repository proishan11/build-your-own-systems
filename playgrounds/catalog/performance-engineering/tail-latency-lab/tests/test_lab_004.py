import unittest

from lab_004 import recover_tail_latency_lab_coordinated_omission


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_compute_percentile_failure(self):
        self.assertEqual(recover_tail_latency_lab_coordinated_omission({'operation': 'compute percentile', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'histogram bucket'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'histogram bucket'})

    def test_fails_permanent_coordinated_omission(self):
        self.assertEqual(recover_tail_latency_lab_coordinated_omission({'operation': 'compute percentile', 'error': 'coordinated omission', 'attempt': 1, 'max_attempts': 3, 'resource': 'histogram bucket'}), {'decision': 'fail', 'reason': 'coordinated omission', 'resource': 'histogram bucket'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_tail_latency_lab_coordinated_omission({'operation': 'compute percentile', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'histogram bucket'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'histogram bucket'})


if __name__ == "__main__":
    unittest.main()
