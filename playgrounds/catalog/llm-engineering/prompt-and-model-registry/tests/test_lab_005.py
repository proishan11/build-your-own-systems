import unittest

from lab_005 import run_prompt_and_model_registry_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_prompt_and_model_registry_happy_path_scenario(self):
        self.assertEqual(run_prompt_and_model_registry_scenario([{'type': 'apply', 'resource': 'model binding', 'value': 'ready'}, {'type': 'metric', 'name': 'versions_published', 'value': 3}, {'type': 'fail', 'reason': 'unsafe prompt change'}, {'type': 'recover', 'reason': 'unsafe prompt change'}]), {'state': {'model binding': 'ready'}, 'metrics': {'versions_published': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_prompt_and_model_registry_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'versions_published': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_prompt_and_model_registry_scenario([]),
            {'state': {}, 'metrics': {'versions_published': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
