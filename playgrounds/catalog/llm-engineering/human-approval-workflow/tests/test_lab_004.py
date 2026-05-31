import unittest

from lab_004 import recover_human_approval_workflow_stale_approval


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_route_approval_failure(self):
        self.assertEqual(recover_human_approval_workflow_stale_approval({'operation': 'route approval', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'approval queue'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'approval queue'})

    def test_fails_permanent_stale_approval(self):
        self.assertEqual(recover_human_approval_workflow_stale_approval({'operation': 'route approval', 'error': 'stale approval', 'attempt': 1, 'max_attempts': 3, 'resource': 'approval queue'}), {'decision': 'fail', 'reason': 'stale approval', 'resource': 'approval queue'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_human_approval_workflow_stale_approval({'operation': 'route approval', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'approval queue'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'approval queue'})


if __name__ == "__main__":
    unittest.main()
