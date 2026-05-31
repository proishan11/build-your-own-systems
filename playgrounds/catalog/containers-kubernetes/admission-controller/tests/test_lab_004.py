import unittest

from lab_004 import recover_admission_controller_policy_bypass


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_admit_object_failure(self):
        self.assertEqual(recover_admission_controller_policy_bypass({'operation': 'admit object', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'policy set'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'policy set'})

    def test_fails_permanent_policy_bypass(self):
        self.assertEqual(recover_admission_controller_policy_bypass({'operation': 'admit object', 'error': 'policy bypass', 'attempt': 1, 'max_attempts': 3, 'resource': 'policy set'}), {'decision': 'fail', 'reason': 'policy bypass', 'resource': 'policy set'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_admission_controller_policy_bypass({'operation': 'admit object', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'policy set'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'policy set'})


if __name__ == "__main__":
    unittest.main()
