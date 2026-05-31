import unittest

from lab_004 import recover_mcp_server_and_client_lab_invalid_json_rpc_id


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_dispatch_tool_failure(self):
        self.assertEqual(recover_mcp_server_and_client_lab_invalid_json_rpc_id({'operation': 'dispatch tool', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'tool registry'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'tool registry'})

    def test_fails_permanent_invalid_json_rpc_id(self):
        self.assertEqual(recover_mcp_server_and_client_lab_invalid_json_rpc_id({'operation': 'dispatch tool', 'error': 'invalid json-rpc id', 'attempt': 1, 'max_attempts': 3, 'resource': 'tool registry'}), {'decision': 'fail', 'reason': 'invalid json-rpc id', 'resource': 'tool registry'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mcp_server_and_client_lab_invalid_json_rpc_id({'operation': 'dispatch tool', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'tool registry'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'tool registry'})


if __name__ == "__main__":
    unittest.main()
