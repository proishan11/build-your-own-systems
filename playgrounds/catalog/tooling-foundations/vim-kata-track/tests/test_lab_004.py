import unittest

from lab_004 import recover_vim_kata_track_off_by_one_cursor


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_apply_motion_failure(self):
        self.assertEqual(recover_vim_kata_track_off_by_one_cursor({'operation': 'apply motion', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'buffer state'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'buffer state'})

    def test_fails_permanent_off_by_one_cursor(self):
        self.assertEqual(recover_vim_kata_track_off_by_one_cursor({'operation': 'apply motion', 'error': 'off-by-one cursor', 'attempt': 1, 'max_attempts': 3, 'resource': 'buffer state'}), {'decision': 'fail', 'reason': 'off-by-one cursor', 'resource': 'buffer state'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_vim_kata_track_off_by_one_cursor({'operation': 'apply motion', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'buffer state'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'buffer state'})


if __name__ == "__main__":
    unittest.main()
