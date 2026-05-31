import unittest

from lab_005 import run_secrets_manager_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_secrets_manager_happy_path_scenario(self):
        self.assertEqual(run_secrets_manager_scenario([{'type': 'apply', 'resource': 'secret store', 'value': 'ready'}, {'type': 'metric', 'name': 'rotations_completed', 'value': 3}, {'type': 'fail', 'reason': 'plaintext exposure'}, {'type': 'recover', 'reason': 'plaintext exposure'}]), {'state': {'secret store': 'ready'}, 'metrics': {'rotations_completed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_secrets_manager_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'rotations_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_secrets_manager_scenario([]),
            {'state': {}, 'metrics': {'rotations_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
