import unittest

from lab_004 import recover_distributed_training_simulator_straggler_worker


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_allreduce_shard_failure(self):
        self.assertEqual(recover_distributed_training_simulator_straggler_worker({'operation': 'allreduce shard', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'worker ring'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'worker ring'})

    def test_fails_permanent_straggler_worker(self):
        self.assertEqual(recover_distributed_training_simulator_straggler_worker({'operation': 'allreduce shard', 'error': 'straggler worker', 'attempt': 1, 'max_attempts': 3, 'resource': 'worker ring'}), {'decision': 'fail', 'reason': 'straggler worker', 'resource': 'worker ring'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_distributed_training_simulator_straggler_worker({'operation': 'allreduce shard', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'worker ring'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'worker ring'})


if __name__ == "__main__":
    unittest.main()
