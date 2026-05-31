import unittest

from lab_005 import run_dynamic_routing_simulator_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_dynamic_routing_simulator_happy_path_scenario(self):
        self.assertEqual(run_dynamic_routing_simulator_scenario([{'type': 'apply', 'resource': 'neighbor table', 'value': 'ready'}, {'type': 'metric', 'name': 'best_routes', 'value': 3}, {'type': 'fail', 'reason': 'routing loop'}, {'type': 'recover', 'reason': 'routing loop'}]), {'state': {'neighbor table': 'ready'}, 'metrics': {'best_routes': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_dynamic_routing_simulator_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'best_routes': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_dynamic_routing_simulator_scenario([]),
            {'state': {}, 'metrics': {'best_routes': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
