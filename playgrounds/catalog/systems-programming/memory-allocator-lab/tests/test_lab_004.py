import unittest

from lab_004 import recover_memory_allocator_lab_double_free


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_split_allocation_failure(self):
        self.assertEqual(recover_memory_allocator_lab_double_free({'operation': 'split allocation', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'free block'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'free block'})

    def test_fails_permanent_double_free(self):
        self.assertEqual(recover_memory_allocator_lab_double_free({'operation': 'split allocation', 'error': 'double free', 'attempt': 1, 'max_attempts': 3, 'resource': 'free block'}), {'decision': 'fail', 'reason': 'double free', 'resource': 'free block'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_memory_allocator_lab_double_free({'operation': 'split allocation', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'free block'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'free block'})


if __name__ == "__main__":
    unittest.main()
