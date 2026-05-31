import unittest

from lab_005 import run_structured_output_validator_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_structured_output_validator_happy_path_scenario(self):
        self.assertEqual(run_structured_output_validator_scenario([{'type': 'apply', 'resource': 'json schema', 'value': 'ready'}, {'type': 'metric', 'name': 'outputs_validated', 'value': 3}, {'type': 'fail', 'reason': 'schema violation'}, {'type': 'recover', 'reason': 'schema violation'}]), {'state': {'json schema': 'ready'}, 'metrics': {'outputs_validated': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_structured_output_validator_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'outputs_validated': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_structured_output_validator_scenario([]),
            {'state': {}, 'metrics': {'outputs_validated': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
