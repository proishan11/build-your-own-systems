import unittest

from lab_003 import plan_agent_security_lab_classify_tools


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_classify_tool_operations(self):
        self.assertEqual(plan_agent_security_lab_classify_tools({'tool-policy-primary': 'ready', 'tool-policy-canary': 'ready'}, {'tool-policy-primary': 'stale', 'tool-policy-old': 'ready'}), [{'op': 'update', 'name': 'tool-policy-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'tool-policy-old', 'from': 'ready'}, {'op': 'create', 'name': 'tool-policy-canary', 'to': 'ready'}])

    def test_noops_when_tool_policy_already_matches(self):
        current = {'tool-policy-primary': 'ready'}
        self.assertEqual(plan_agent_security_lab_classify_tools(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_agent_security_lab_classify_tools({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
