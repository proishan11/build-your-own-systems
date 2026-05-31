import unittest

from lab_005 import run_layer_4_load_balancer_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_layer_4_load_balancer_happy_path_scenario(self):
        self.assertEqual(run_layer_4_load_balancer_scenario([{'type': 'apply', 'resource': 'backend pool', 'value': 'ready'}, {'type': 'metric', 'name': 'active_flows', 'value': 3}, {'type': 'fail', 'reason': 'unhealthy backend'}, {'type': 'recover', 'reason': 'unhealthy backend'}]), {'state': {'backend pool': 'ready'}, 'metrics': {'active_flows': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_layer_4_load_balancer_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'active_flows': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_layer_4_load_balancer_scenario([]),
            {'state': {}, 'metrics': {'active_flows': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
