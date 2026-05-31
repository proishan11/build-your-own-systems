import unittest

from lab_004 import recover_mapreduce_runtime_worker_crash


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_schedule_task_failure(self):
        self.assertEqual(recover_mapreduce_runtime_worker_crash({'operation': 'schedule task', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'task tracker'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'task tracker'})

    def test_fails_permanent_worker_crash(self):
        self.assertEqual(recover_mapreduce_runtime_worker_crash({'operation': 'schedule task', 'error': 'worker crash', 'attempt': 1, 'max_attempts': 3, 'resource': 'task tracker'}), {'decision': 'fail', 'reason': 'worker crash', 'resource': 'task tracker'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mapreduce_runtime_worker_crash({'operation': 'schedule task', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'task tracker'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'task tracker'})


if __name__ == "__main__":
    unittest.main()
