import unittest

from lab_004 import recover_dynamo_style_kv_store_sibling_conflict


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_write_quorum_failure(self):
        self.assertEqual(recover_dynamo_style_kv_store_sibling_conflict({'operation': 'write quorum', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'replica set'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'replica set'})

    def test_fails_permanent_sibling_conflict(self):
        self.assertEqual(recover_dynamo_style_kv_store_sibling_conflict({'operation': 'write quorum', 'error': 'sibling conflict', 'attempt': 1, 'max_attempts': 3, 'resource': 'replica set'}), {'decision': 'fail', 'reason': 'sibling conflict', 'resource': 'replica set'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_dynamo_style_kv_store_sibling_conflict({'operation': 'write quorum', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'replica set'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'replica set'})


if __name__ == "__main__":
    unittest.main()
