import unittest

from lab_004 import recover_agent_security_lab_secret_exfiltration


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_classify_tool_failure(self):
        self.assertEqual(recover_agent_security_lab_secret_exfiltration({'operation': 'classify tool', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'tool policy'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'tool policy'})

    def test_fails_permanent_secret_exfiltration(self):
        self.assertEqual(recover_agent_security_lab_secret_exfiltration({'operation': 'classify tool', 'error': 'secret exfiltration', 'attempt': 1, 'max_attempts': 3, 'resource': 'tool policy'}), {'decision': 'fail', 'reason': 'secret exfiltration', 'resource': 'tool policy'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_agent_security_lab_secret_exfiltration({'operation': 'classify tool', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'tool policy'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'tool policy'})


if __name__ == "__main__":
    unittest.main()
