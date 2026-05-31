import unittest

from lab_005 import run_vulnerable_web_app_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_vulnerable_web_app_lab_happy_path_scenario(self):
        self.assertEqual(run_vulnerable_web_app_lab_scenario([{'type': 'apply', 'resource': 'security policy', 'value': 'ready'}, {'type': 'metric', 'name': 'requests_blocked', 'value': 3}, {'type': 'fail', 'reason': 'xss payload'}, {'type': 'recover', 'reason': 'xss payload'}]), {'state': {'security policy': 'ready'}, 'metrics': {'requests_blocked': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_vulnerable_web_app_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'requests_blocked': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_vulnerable_web_app_lab_scenario([]),
            {'state': {}, 'metrics': {'requests_blocked': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
