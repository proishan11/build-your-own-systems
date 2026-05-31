import unittest

from lab_004 import recover_query_performance_lab_write_amplification


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_recommend_index_failure(self):
        self.assertEqual(recover_query_performance_lab_write_amplification({'operation': 'recommend index', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'index catalog'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'index catalog'})

    def test_fails_permanent_write_amplification(self):
        self.assertEqual(recover_query_performance_lab_write_amplification({'operation': 'recommend index', 'error': 'write amplification', 'attempt': 1, 'max_attempts': 3, 'resource': 'index catalog'}), {'decision': 'fail', 'reason': 'write amplification', 'resource': 'index catalog'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_query_performance_lab_write_amplification({'operation': 'recommend index', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'index catalog'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'index catalog'})


if __name__ == "__main__":
    unittest.main()
