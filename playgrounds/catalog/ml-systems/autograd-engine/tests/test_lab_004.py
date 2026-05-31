import unittest

from lab_004 import recover_autograd_engine_shape_mismatch


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_backpropagate_gradient_failure(self):
        self.assertEqual(recover_autograd_engine_shape_mismatch({'operation': 'backpropagate gradient', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'computation graph'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'computation graph'})

    def test_fails_permanent_shape_mismatch(self):
        self.assertEqual(recover_autograd_engine_shape_mismatch({'operation': 'backpropagate gradient', 'error': 'shape mismatch', 'attempt': 1, 'max_attempts': 3, 'resource': 'computation graph'}), {'decision': 'fail', 'reason': 'shape mismatch', 'resource': 'computation graph'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_autograd_engine_shape_mismatch({'operation': 'backpropagate gradient', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'computation graph'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'computation graph'})


if __name__ == "__main__":
    unittest.main()
