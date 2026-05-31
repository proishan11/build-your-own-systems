import unittest

from lab_004 import recover_mini_shell_with_job_control_orphaned_background_job


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_spawn_job_failure(self):
        self.assertEqual(recover_mini_shell_with_job_control_orphaned_background_job({'operation': 'spawn job', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'process group'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'process group'})

    def test_fails_permanent_orphaned_background_job(self):
        self.assertEqual(recover_mini_shell_with_job_control_orphaned_background_job({'operation': 'spawn job', 'error': 'orphaned background job', 'attempt': 1, 'max_attempts': 3, 'resource': 'process group'}), {'decision': 'fail', 'reason': 'orphaned background job', 'resource': 'process group'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mini_shell_with_job_control_orphaned_background_job({'operation': 'spawn job', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'process group'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'process group'})


if __name__ == "__main__":
    unittest.main()
