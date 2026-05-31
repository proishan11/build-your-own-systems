import unittest

from lab_004 import recover_agent_runtime_infinite_loop


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_choose_tool_failure(self):
        self.assertEqual(recover_agent_runtime_infinite_loop({'operation': 'choose tool', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'execution trace'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'execution trace'})

    def test_fails_permanent_infinite_loop(self):
        self.assertEqual(recover_agent_runtime_infinite_loop({'operation': 'choose tool', 'error': 'infinite loop', 'attempt': 1, 'max_attempts': 3, 'resource': 'execution trace'}), {'decision': 'fail', 'reason': 'infinite loop', 'resource': 'execution trace'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_agent_runtime_infinite_loop({'operation': 'choose tool', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'execution trace'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'execution trace'})


if __name__ == "__main__":
    unittest.main()
