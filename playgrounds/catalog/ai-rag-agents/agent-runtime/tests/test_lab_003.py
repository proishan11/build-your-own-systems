import unittest

from lab_003 import plan_agent_runtime_choose_tools


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_choose_tool_operations(self):
        self.assertEqual(plan_agent_runtime_choose_tools({'execution-trace-primary': 'ready', 'execution-trace-canary': 'ready'}, {'execution-trace-primary': 'stale', 'execution-trace-old': 'ready'}), [{'op': 'update', 'name': 'execution-trace-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'execution-trace-old', 'from': 'ready'}, {'op': 'create', 'name': 'execution-trace-canary', 'to': 'ready'}])

    def test_noops_when_execution_trace_already_matches(self):
        current = {'execution-trace-primary': 'ready'}
        self.assertEqual(plan_agent_runtime_choose_tools(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_agent_runtime_choose_tools({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
