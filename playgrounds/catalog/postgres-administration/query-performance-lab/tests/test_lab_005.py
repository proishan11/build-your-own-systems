import unittest

from lab_005 import run_query_performance_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_query_performance_lab_happy_path_scenario(self):
        self.assertEqual(run_query_performance_lab_scenario([{'type': 'apply', 'resource': 'index catalog', 'value': 'ready'}, {'type': 'metric', 'name': 'cost_reduction', 'value': 3}, {'type': 'fail', 'reason': 'write amplification'}, {'type': 'recover', 'reason': 'write amplification'}]), {'state': {'index catalog': 'ready'}, 'metrics': {'cost_reduction': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_query_performance_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'cost_reduction': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_query_performance_lab_scenario([]),
            {'state': {}, 'metrics': {'cost_reduction': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
