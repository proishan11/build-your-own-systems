import unittest

from lab_004 import recover_git_merge_and_rebase_lab_conflict_marker_leak


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_resolve_merge_failure(self):
        self.assertEqual(recover_git_merge_and_rebase_lab_conflict_marker_leak({'operation': 'resolve merge', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'merge graph'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'merge graph'})

    def test_fails_permanent_conflict_marker_leak(self):
        self.assertEqual(recover_git_merge_and_rebase_lab_conflict_marker_leak({'operation': 'resolve merge', 'error': 'conflict marker leak', 'attempt': 1, 'max_attempts': 3, 'resource': 'merge graph'}), {'decision': 'fail', 'reason': 'conflict marker leak', 'resource': 'merge graph'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_git_merge_and_rebase_lab_conflict_marker_leak({'operation': 'resolve merge', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'merge graph'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'merge graph'})


if __name__ == "__main__":
    unittest.main()
