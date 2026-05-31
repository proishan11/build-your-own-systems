import unittest

from lab_005 import run_feature_store_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_feature_store_happy_path_scenario(self):
        self.assertEqual(run_feature_store_scenario([{'type': 'apply', 'resource': 'feature registry', 'value': 'ready'}, {'type': 'metric', 'name': 'fresh_rows', 'value': 3}, {'type': 'fail', 'reason': 'stale feature'}, {'type': 'recover', 'reason': 'stale feature'}]), {'state': {'feature registry': 'ready'}, 'metrics': {'fresh_rows': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_feature_store_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'fresh_rows': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_feature_store_scenario([]),
            {'state': {}, 'metrics': {'fresh_rows': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
