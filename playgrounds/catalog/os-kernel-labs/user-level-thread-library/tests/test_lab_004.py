import unittest

from lab_004 import recover_user_level_thread_library_lost_wakeup


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_yield_thread_failure(self):
        self.assertEqual(recover_user_level_thread_library_lost_wakeup({'operation': 'yield thread', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'run queue'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'run queue'})

    def test_fails_permanent_lost_wakeup(self):
        self.assertEqual(recover_user_level_thread_library_lost_wakeup({'operation': 'yield thread', 'error': 'lost wakeup', 'attempt': 1, 'max_attempts': 3, 'resource': 'run queue'}), {'decision': 'fail', 'reason': 'lost wakeup', 'resource': 'run queue'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_user_level_thread_library_lost_wakeup({'operation': 'yield thread', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'run queue'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'run queue'})


if __name__ == "__main__":
    unittest.main()
