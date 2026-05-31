import unittest

from lab_003 import plan_sandboxed_coding_agent_authorize_tools


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_authorize_tool_operations(self):
        self.assertEqual(plan_sandboxed_coding_agent_authorize_tools({'sandbox-policy-primary': 'ready', 'sandbox-policy-canary': 'ready'}, {'sandbox-policy-primary': 'stale', 'sandbox-policy-old': 'ready'}), [{'op': 'update', 'name': 'sandbox-policy-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'sandbox-policy-old', 'from': 'ready'}, {'op': 'create', 'name': 'sandbox-policy-canary', 'to': 'ready'}])

    def test_noops_when_sandbox_policy_already_matches(self):
        current = {'sandbox-policy-primary': 'ready'}
        self.assertEqual(plan_sandboxed_coding_agent_authorize_tools(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_sandboxed_coding_agent_authorize_tools({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
