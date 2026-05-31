import unittest

from lab_004 import recover_virtual_memory_simulator_permission_fault


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_map_page_failure(self):
        self.assertEqual(recover_virtual_memory_simulator_permission_fault({'operation': 'map page', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'page table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'page table'})

    def test_fails_permanent_permission_fault(self):
        self.assertEqual(recover_virtual_memory_simulator_permission_fault({'operation': 'map page', 'error': 'permission fault', 'attempt': 1, 'max_attempts': 3, 'resource': 'page table'}), {'decision': 'fail', 'reason': 'permission fault', 'resource': 'page table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_virtual_memory_simulator_permission_fault({'operation': 'map page', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'page table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'page table'})


if __name__ == "__main__":
    unittest.main()
