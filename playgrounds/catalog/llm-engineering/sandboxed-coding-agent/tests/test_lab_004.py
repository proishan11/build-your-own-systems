import unittest

from lab_004 import recover_sandboxed_coding_agent_filesystem_escape


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_authorize_tool_failure(self):
        self.assertEqual(recover_sandboxed_coding_agent_filesystem_escape({'operation': 'authorize tool', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'sandbox policy'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'sandbox policy'})

    def test_fails_permanent_filesystem_escape(self):
        self.assertEqual(recover_sandboxed_coding_agent_filesystem_escape({'operation': 'authorize tool', 'error': 'filesystem escape', 'attempt': 1, 'max_attempts': 3, 'resource': 'sandbox policy'}), {'decision': 'fail', 'reason': 'filesystem escape', 'resource': 'sandbox policy'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_sandboxed_coding_agent_filesystem_escape({'operation': 'authorize tool', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'sandbox policy'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'sandbox policy'})


if __name__ == "__main__":
    unittest.main()
