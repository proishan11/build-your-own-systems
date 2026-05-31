import unittest

from lab_005 import run_vim_kata_track_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_vim_kata_track_happy_path_scenario(self):
        self.assertEqual(run_vim_kata_track_scenario([{'type': 'apply', 'resource': 'buffer state', 'value': 'ready'}, {'type': 'metric', 'name': 'motions_applied', 'value': 3}, {'type': 'fail', 'reason': 'off-by-one cursor'}, {'type': 'recover', 'reason': 'off-by-one cursor'}]), {'state': {'buffer state': 'ready'}, 'metrics': {'motions_applied': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_vim_kata_track_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'motions_applied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_vim_kata_track_scenario([]),
            {'state': {}, 'metrics': {'motions_applied': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
