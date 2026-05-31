import unittest

from lab_005 import run_nat_gateway_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_nat_gateway_happy_path_scenario(self):
        self.assertEqual(run_nat_gateway_scenario([{'type': 'apply', 'resource': 'translation table', 'value': 'ready'}, {'type': 'metric', 'name': 'translations_active', 'value': 3}, {'type': 'fail', 'reason': 'port exhaustion'}, {'type': 'recover', 'reason': 'port exhaustion'}]), {'state': {'translation table': 'ready'}, 'metrics': {'translations_active': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_nat_gateway_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'translations_active': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_nat_gateway_scenario([]),
            {'state': {}, 'metrics': {'translations_active': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
