import unittest

from lab_005 import run_agent_security_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_agent_security_lab_happy_path_scenario(self):
        self.assertEqual(run_agent_security_lab_scenario([{'type': 'apply', 'resource': 'tool policy', 'value': 'ready'}, {'type': 'metric', 'name': 'calls_denied', 'value': 3}, {'type': 'fail', 'reason': 'secret exfiltration'}, {'type': 'recover', 'reason': 'secret exfiltration'}]), {'state': {'tool policy': 'ready'}, 'metrics': {'calls_denied': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_agent_security_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'calls_denied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_agent_security_lab_scenario([]),
            {'state': {}, 'metrics': {'calls_denied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
