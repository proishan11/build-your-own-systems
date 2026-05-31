import unittest

from lab_004 import recover_container_registry_digest_mismatch


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_serve_manifest_failure(self):
        self.assertEqual(recover_container_registry_digest_mismatch({'operation': 'serve manifest', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'blob store'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'blob store'})

    def test_fails_permanent_digest_mismatch(self):
        self.assertEqual(recover_container_registry_digest_mismatch({'operation': 'serve manifest', 'error': 'digest mismatch', 'attempt': 1, 'max_attempts': 3, 'resource': 'blob store'}), {'decision': 'fail', 'reason': 'digest mismatch', 'resource': 'blob store'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_container_registry_digest_mismatch({'operation': 'serve manifest', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'blob store'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'blob store'})


if __name__ == "__main__":
    unittest.main()
