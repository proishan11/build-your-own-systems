import unittest

from lab_005 import run_mini_git_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_mini_git_happy_path_scenario(self):
        self.assertEqual(run_mini_git_scenario([{'type': 'apply', 'resource': 'object database', 'value': 'ready'}, {'type': 'metric', 'name': 'objects_written', 'value': 3}, {'type': 'fail', 'reason': 'hash mismatch'}, {'type': 'recover', 'reason': 'hash mismatch'}]), {'state': {'object database': 'ready'}, 'metrics': {'objects_written': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_mini_git_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'objects_written': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_mini_git_scenario([]),
            {'state': {}, 'metrics': {'objects_written': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
