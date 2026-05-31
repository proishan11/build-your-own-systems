import unittest

from lab_004 import recover_coreutils_from_scratch_binary_input


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_transform_stream_failure(self):
        self.assertEqual(recover_coreutils_from_scratch_binary_input({'operation': 'transform stream', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'command input'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'command input'})

    def test_fails_permanent_binary_input(self):
        self.assertEqual(recover_coreutils_from_scratch_binary_input({'operation': 'transform stream', 'error': 'binary input', 'attempt': 1, 'max_attempts': 3, 'resource': 'command input'}), {'decision': 'fail', 'reason': 'binary input', 'resource': 'command input'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_coreutils_from_scratch_binary_input({'operation': 'transform stream', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'command input'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'command input'})


if __name__ == "__main__":
    unittest.main()
