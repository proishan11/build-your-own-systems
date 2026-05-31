import unittest

from lab_005 import run_model_registry_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_model_registry_happy_path_scenario(self):
        self.assertEqual(run_model_registry_scenario([{'type': 'apply', 'resource': 'registry version', 'value': 'ready'}, {'type': 'metric', 'name': 'models_promoted', 'value': 3}, {'type': 'fail', 'reason': 'missing lineage'}, {'type': 'recover', 'reason': 'missing lineage'}]), {'state': {'registry version': 'ready'}, 'metrics': {'models_promoted': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_model_registry_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'models_promoted': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_model_registry_scenario([]),
            {'state': {}, 'metrics': {'models_promoted': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
