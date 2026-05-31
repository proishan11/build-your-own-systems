import unittest

from lab_005 import run_git_merge_and_rebase_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_git_merge_and_rebase_lab_happy_path_scenario(self):
        self.assertEqual(run_git_merge_and_rebase_lab_scenario([{'type': 'apply', 'resource': 'merge graph', 'value': 'ready'}, {'type': 'metric', 'name': 'conflicts_resolved', 'value': 3}, {'type': 'fail', 'reason': 'conflict marker leak'}, {'type': 'recover', 'reason': 'conflict marker leak'}]), {'state': {'merge graph': 'ready'}, 'metrics': {'conflicts_resolved': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_git_merge_and_rebase_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'conflicts_resolved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_git_merge_and_rebase_lab_scenario([]),
            {'state': {}, 'metrics': {'conflicts_resolved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
