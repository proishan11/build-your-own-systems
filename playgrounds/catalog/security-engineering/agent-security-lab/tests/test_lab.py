import unittest

from lab import classify_tool_agent_tool_call


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_agent_tool_call_request(self):
        self.assertEqual(classify_tool_agent_tool_call({'id': 'agent-tool-call-001', 'kind': 'classify tool', 'target': 'tool policy', 'priority': 2, 'metadata': {'source': 'Agent Security Lab', 'track': 'security-engineering'}}), {'id': 'agent-tool-call-001', 'action': 'classify tool', 'target': 'tool policy', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_agent_tool_call_request(self):
        self.assertEqual(classify_tool_agent_tool_call({'id': 'bad', 'kind': '', 'target': 'tool policy', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'tool policy', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'agent-tool-call-001', 'kind': 'classify tool', 'target': 'tool policy', 'priority': 2, 'metadata': {'source': 'Agent Security Lab', 'track': 'security-engineering'}}
        original = dict(request)
        classify_tool_agent_tool_call(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
