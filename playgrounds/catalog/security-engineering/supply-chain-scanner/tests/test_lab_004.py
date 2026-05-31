import unittest

from lab_004 import recover_supply_chain_scanner_unsigned_dependency


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_scan_artifact_failure(self):
        self.assertEqual(recover_supply_chain_scanner_unsigned_dependency({'operation': 'scan artifact', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'sbom index'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'sbom index'})

    def test_fails_permanent_unsigned_dependency(self):
        self.assertEqual(recover_supply_chain_scanner_unsigned_dependency({'operation': 'scan artifact', 'error': 'unsigned dependency', 'attempt': 1, 'max_attempts': 3, 'resource': 'sbom index'}), {'decision': 'fail', 'reason': 'unsigned dependency', 'resource': 'sbom index'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_supply_chain_scanner_unsigned_dependency({'operation': 'scan artifact', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'sbom index'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'sbom index'})


if __name__ == "__main__":
    unittest.main()
