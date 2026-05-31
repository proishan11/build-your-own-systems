import unittest

from lab_004 import recover_feature_flag_and_rollout_system_bad_percentage_rollout


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_evaluate_flag_failure(self):
        self.assertEqual(recover_feature_flag_and_rollout_system_bad_percentage_rollout({'operation': 'evaluate flag', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'rollout rule'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'rollout rule'})

    def test_fails_permanent_bad_percentage_rollout(self):
        self.assertEqual(recover_feature_flag_and_rollout_system_bad_percentage_rollout({'operation': 'evaluate flag', 'error': 'bad percentage rollout', 'attempt': 1, 'max_attempts': 3, 'resource': 'rollout rule'}), {'decision': 'fail', 'reason': 'bad percentage rollout', 'resource': 'rollout rule'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_feature_flag_and_rollout_system_bad_percentage_rollout({'operation': 'evaluate flag', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'rollout rule'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'rollout rule'})


if __name__ == "__main__":
    unittest.main()
