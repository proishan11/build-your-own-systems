import unittest

from lab import choose_tool_agent_step


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_agent_step_request(self):
        self.assertEqual(choose_tool_agent_step({'id': 'agent-step-001', 'kind': 'choose tool', 'target': 'execution trace', 'priority': 2, 'metadata': {'source': 'Agent Runtime', 'track': 'ai-rag-agents'}}), {'id': 'agent-step-001', 'action': 'choose tool', 'target': 'execution trace', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_agent_step_request(self):
        self.assertEqual(choose_tool_agent_step({'id': 'bad', 'kind': '', 'target': 'execution trace', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'execution trace', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'agent-step-001', 'kind': 'choose tool', 'target': 'execution trace', 'priority': 2, 'metadata': {'source': 'Agent Runtime', 'track': 'ai-rag-agents'}}
        original = dict(request)
        choose_tool_agent_step(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
