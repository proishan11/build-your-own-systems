import unittest

from lab import dispatch_tool_mcp_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_mcp_request_request(self):
        self.assertEqual(dispatch_tool_mcp_request({'id': 'mcp-request-001', 'kind': 'dispatch tool', 'target': 'tool registry', 'priority': 2, 'metadata': {'source': 'MCP Server and Client Lab', 'track': 'ai-rag-agents'}}), {'id': 'mcp-request-001', 'action': 'dispatch tool', 'target': 'tool registry', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_mcp_request_request(self):
        self.assertEqual(dispatch_tool_mcp_request({'id': 'bad', 'kind': '', 'target': 'tool registry', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'tool registry', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'mcp-request-001', 'kind': 'dispatch tool', 'target': 'tool registry', 'priority': 2, 'metadata': {'source': 'MCP Server and Client Lab', 'track': 'ai-rag-agents'}}
        original = dict(request)
        dispatch_tool_mcp_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
