import unittest

from lab_005 import run_admission_controller_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_admission_controller_happy_path_scenario(self):
        self.assertEqual(run_admission_controller_scenario([{'type': 'apply', 'resource': 'policy set', 'value': 'ready'}, {'type': 'metric', 'name': 'requests_denied', 'value': 3}, {'type': 'fail', 'reason': 'policy bypass'}, {'type': 'recover', 'reason': 'policy bypass'}]), {'state': {'policy set': 'ready'}, 'metrics': {'requests_denied': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_admission_controller_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'requests_denied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_admission_controller_scenario([]),
            {'state': {}, 'metrics': {'requests_denied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
