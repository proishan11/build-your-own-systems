import unittest

from lab_004 import recover_minidb_storage_engine_dirty_page_loss


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_write_record_failure(self):
        self.assertEqual(recover_minidb_storage_engine_dirty_page_loss({'operation': 'write record', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'page cache'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'page cache'})

    def test_fails_permanent_dirty_page_loss(self):
        self.assertEqual(recover_minidb_storage_engine_dirty_page_loss({'operation': 'write record', 'error': 'dirty page loss', 'attempt': 1, 'max_attempts': 3, 'resource': 'page cache'}), {'decision': 'fail', 'reason': 'dirty page loss', 'resource': 'page cache'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_minidb_storage_engine_dirty_page_loss({'operation': 'write record', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'page cache'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'page cache'})


if __name__ == "__main__":
    unittest.main()
