import unittest

from lab_005 import run_sandboxed_coding_agent_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_sandboxed_coding_agent_happy_path_scenario(self):
        self.assertEqual(run_sandboxed_coding_agent_scenario([{'type': 'apply', 'resource': 'sandbox policy', 'value': 'ready'}, {'type': 'metric', 'name': 'tool_calls_allowed', 'value': 3}, {'type': 'fail', 'reason': 'filesystem escape'}, {'type': 'recover', 'reason': 'filesystem escape'}]), {'state': {'sandbox policy': 'ready'}, 'metrics': {'tool_calls_allowed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_sandboxed_coding_agent_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'tool_calls_allowed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_sandboxed_coding_agent_scenario([]),
            {'state': {}, 'metrics': {'tool_calls_allowed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
