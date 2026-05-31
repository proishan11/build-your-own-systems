import unittest

from lab_005 import run_feature_flag_and_rollout_system_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_feature_flag_and_rollout_system_happy_path_scenario(self):
        self.assertEqual(run_feature_flag_and_rollout_system_scenario([{'type': 'apply', 'resource': 'rollout rule', 'value': 'ready'}, {'type': 'metric', 'name': 'evaluations_served', 'value': 3}, {'type': 'fail', 'reason': 'bad percentage rollout'}, {'type': 'recover', 'reason': 'bad percentage rollout'}]), {'state': {'rollout rule': 'ready'}, 'metrics': {'evaluations_served': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_feature_flag_and_rollout_system_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'evaluations_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_feature_flag_and_rollout_system_scenario([]),
            {'state': {}, 'metrics': {'evaluations_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
