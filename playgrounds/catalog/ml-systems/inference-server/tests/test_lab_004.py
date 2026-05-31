import unittest

from lab_004 import recover_inference_server_deadline_miss


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_batch_request_failure(self):
        self.assertEqual(recover_inference_server_deadline_miss({'operation': 'batch request', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'batch queue'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'batch queue'})

    def test_fails_permanent_deadline_miss(self):
        self.assertEqual(recover_inference_server_deadline_miss({'operation': 'batch request', 'error': 'deadline miss', 'attempt': 1, 'max_attempts': 3, 'resource': 'batch queue'}), {'decision': 'fail', 'reason': 'deadline miss', 'resource': 'batch queue'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_inference_server_deadline_miss({'operation': 'batch request', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'batch queue'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'batch queue'})


if __name__ == "__main__":
    unittest.main()
