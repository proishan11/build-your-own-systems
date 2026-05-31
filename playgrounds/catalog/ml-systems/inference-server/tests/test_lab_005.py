import unittest

from lab_005 import run_inference_server_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_inference_server_happy_path_scenario(self):
        self.assertEqual(run_inference_server_scenario([{'type': 'apply', 'resource': 'batch queue', 'value': 'ready'}, {'type': 'metric', 'name': 'tokens_served', 'value': 3}, {'type': 'fail', 'reason': 'deadline miss'}, {'type': 'recover', 'reason': 'deadline miss'}]), {'state': {'batch queue': 'ready'}, 'metrics': {'tokens_served': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_inference_server_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'tokens_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_inference_server_scenario([]),
            {'state': {}, 'metrics': {'tokens_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
