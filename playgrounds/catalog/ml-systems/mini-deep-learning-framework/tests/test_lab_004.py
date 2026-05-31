import unittest

from lab_004 import recover_mini_deep_learning_framework_nan_gradient


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_run_forward_pass_failure(self):
        self.assertEqual(recover_mini_deep_learning_framework_nan_gradient({'operation': 'run forward pass', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'module graph'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'module graph'})

    def test_fails_permanent_nan_gradient(self):
        self.assertEqual(recover_mini_deep_learning_framework_nan_gradient({'operation': 'run forward pass', 'error': 'nan gradient', 'attempt': 1, 'max_attempts': 3, 'resource': 'module graph'}), {'decision': 'fail', 'reason': 'nan gradient', 'resource': 'module graph'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mini_deep_learning_framework_nan_gradient({'operation': 'run forward pass', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'module graph'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'module graph'})


if __name__ == "__main__":
    unittest.main()
