import unittest

from lab import authorize_tool_tool_invocation


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_tool_invocation_request(self):
        self.assertEqual(authorize_tool_tool_invocation({'id': 'tool-invocation-001', 'kind': 'authorize tool', 'target': 'sandbox policy', 'priority': 2, 'metadata': {'source': 'Sandboxed Coding Agent', 'track': 'llm-engineering'}}), {'id': 'tool-invocation-001', 'action': 'authorize tool', 'target': 'sandbox policy', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_tool_invocation_request(self):
        self.assertEqual(authorize_tool_tool_invocation({'id': 'bad', 'kind': '', 'target': 'sandbox policy', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'sandbox policy', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'tool-invocation-001', 'kind': 'authorize tool', 'target': 'sandbox policy', 'priority': 2, 'metadata': {'source': 'Sandboxed Coding Agent', 'track': 'llm-engineering'}}
        original = dict(request)
        authorize_tool_tool_invocation(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
