import unittest

from lab_004 import recover_feature_store_stale_feature


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_materialize_feature_failure(self):
        self.assertEqual(recover_feature_store_stale_feature({'operation': 'materialize feature', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'feature registry'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'feature registry'})

    def test_fails_permanent_stale_feature(self):
        self.assertEqual(recover_feature_store_stale_feature({'operation': 'materialize feature', 'error': 'stale feature', 'attempt': 1, 'max_attempts': 3, 'resource': 'feature registry'}), {'decision': 'fail', 'reason': 'stale feature', 'resource': 'feature registry'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_feature_store_stale_feature({'operation': 'materialize feature', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'feature registry'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'feature registry'})


if __name__ == "__main__":
    unittest.main()
