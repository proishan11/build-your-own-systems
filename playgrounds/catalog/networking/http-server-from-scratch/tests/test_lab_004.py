import unittest

from lab_004 import recover_http_server_from_scratch_malformed_header


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_dispatch_handler_failure(self):
        self.assertEqual(recover_http_server_from_scratch_malformed_header({'operation': 'dispatch handler', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'route table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'route table'})

    def test_fails_permanent_malformed_header(self):
        self.assertEqual(recover_http_server_from_scratch_malformed_header({'operation': 'dispatch handler', 'error': 'malformed header', 'attempt': 1, 'max_attempts': 3, 'resource': 'route table'}), {'decision': 'fail', 'reason': 'malformed header', 'resource': 'route table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_http_server_from_scratch_malformed_header({'operation': 'dispatch handler', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'route table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'route table'})


if __name__ == "__main__":
    unittest.main()
