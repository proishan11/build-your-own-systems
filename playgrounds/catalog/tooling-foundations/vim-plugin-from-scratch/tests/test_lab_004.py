import unittest

from lab_004 import recover_vim_plugin_from_scratch_recursive_mapping


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_handle_autocmd_failure(self):
        self.assertEqual(recover_vim_plugin_from_scratch_recursive_mapping({'operation': 'handle autocmd', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'editor state'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'editor state'})

    def test_fails_permanent_recursive_mapping(self):
        self.assertEqual(recover_vim_plugin_from_scratch_recursive_mapping({'operation': 'handle autocmd', 'error': 'recursive mapping', 'attempt': 1, 'max_attempts': 3, 'resource': 'editor state'}), {'decision': 'fail', 'reason': 'recursive mapping', 'resource': 'editor state'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_vim_plugin_from_scratch_recursive_mapping({'operation': 'handle autocmd', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'editor state'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'editor state'})


if __name__ == "__main__":
    unittest.main()
