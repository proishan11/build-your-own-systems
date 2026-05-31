import unittest

from lab_005 import run_autograd_engine_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_autograd_engine_happy_path_scenario(self):
        self.assertEqual(run_autograd_engine_scenario([{'type': 'apply', 'resource': 'computation graph', 'value': 'ready'}, {'type': 'metric', 'name': 'nodes_visited', 'value': 3}, {'type': 'fail', 'reason': 'shape mismatch'}, {'type': 'recover', 'reason': 'shape mismatch'}]), {'state': {'computation graph': 'ready'}, 'metrics': {'nodes_visited': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_autograd_engine_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'nodes_visited': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_autograd_engine_scenario([]),
            {'state': {}, 'metrics': {'nodes_visited': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
