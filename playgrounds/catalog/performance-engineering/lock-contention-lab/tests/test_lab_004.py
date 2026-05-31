import unittest

from lab_004 import recover_lock_contention_lab_convoy_effect


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_attribute_wait_failure(self):
        self.assertEqual(recover_lock_contention_lab_convoy_effect({'operation': 'attribute wait', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'wait graph'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'wait graph'})

    def test_fails_permanent_convoy_effect(self):
        self.assertEqual(recover_lock_contention_lab_convoy_effect({'operation': 'attribute wait', 'error': 'convoy effect', 'attempt': 1, 'max_attempts': 3, 'resource': 'wait graph'}), {'decision': 'fail', 'reason': 'convoy effect', 'resource': 'wait graph'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_lock_contention_lab_convoy_effect({'operation': 'attribute wait', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'wait graph'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'wait graph'})


if __name__ == "__main__":
    unittest.main()
