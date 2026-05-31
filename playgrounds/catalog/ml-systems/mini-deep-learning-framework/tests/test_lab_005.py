import unittest

from lab_005 import run_mini_deep_learning_framework_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_mini_deep_learning_framework_happy_path_scenario(self):
        self.assertEqual(run_mini_deep_learning_framework_scenario([{'type': 'apply', 'resource': 'module graph', 'value': 'ready'}, {'type': 'metric', 'name': 'loss_value', 'value': 3}, {'type': 'fail', 'reason': 'nan gradient'}, {'type': 'recover', 'reason': 'nan gradient'}]), {'state': {'module graph': 'ready'}, 'metrics': {'loss_value': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_mini_deep_learning_framework_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'loss_value': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_mini_deep_learning_framework_scenario([]),
            {'state': {}, 'metrics': {'loss_value': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
