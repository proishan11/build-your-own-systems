import unittest

from lab_003 import plan_mcp_server_and_client_lab_dispatch_tools


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_dispatch_tool_operations(self):
        self.assertEqual(plan_mcp_server_and_client_lab_dispatch_tools({'tool-registry-primary': 'ready', 'tool-registry-canary': 'ready'}, {'tool-registry-primary': 'stale', 'tool-registry-old': 'ready'}), [{'op': 'update', 'name': 'tool-registry-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'tool-registry-old', 'from': 'ready'}, {'op': 'create', 'name': 'tool-registry-canary', 'to': 'ready'}])

    def test_noops_when_tool_registry_already_matches(self):
        current = {'tool-registry-primary': 'ready'}
        self.assertEqual(plan_mcp_server_and_client_lab_dispatch_tools(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mcp_server_and_client_lab_dispatch_tools({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
