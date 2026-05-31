import unittest

from lab_005 import run_kubernetes_controller_from_scratch_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_kubernetes_controller_from_scratch_happy_path_scenario(self):
        self.assertEqual(run_kubernetes_controller_from_scratch_scenario([{'type': 'apply', 'resource': 'reconcile state', 'value': 'ready'}, {'type': 'metric', 'name': 'reconciles_total', 'value': 3}, {'type': 'fail', 'reason': 'stale observed generation'}, {'type': 'recover', 'reason': 'stale observed generation'}]), {'state': {'reconcile state': 'ready'}, 'metrics': {'reconciles_total': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_kubernetes_controller_from_scratch_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'reconciles_total': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_kubernetes_controller_from_scratch_scenario([]),
            {'state': {}, 'metrics': {'reconciles_total': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
