import unittest

from lab_005 import run_model_router_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_model_router_happy_path_scenario(self):
        self.assertEqual(run_model_router_scenario([{'type': 'apply', 'resource': 'model catalog', 'value': 'ready'}, {'type': 'metric', 'name': 'requests_routed', 'value': 3}, {'type': 'fail', 'reason': 'context overflow'}, {'type': 'recover', 'reason': 'context overflow'}]), {'state': {'model catalog': 'ready'}, 'metrics': {'requests_routed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_model_router_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'requests_routed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_model_router_scenario([]),
            {'state': {}, 'metrics': {'requests_routed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
