import unittest

from lab_005 import run_go_concurrency_gauntlet_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_go_concurrency_gauntlet_happy_path_scenario(self):
        self.assertEqual(run_go_concurrency_gauntlet_scenario([{'type': 'apply', 'resource': 'worker group', 'value': 'ready'}, {'type': 'metric', 'name': 'goroutines_active', 'value': 3}, {'type': 'fail', 'reason': 'blocked sender'}, {'type': 'recover', 'reason': 'blocked sender'}]), {'state': {'worker group': 'ready'}, 'metrics': {'goroutines_active': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_go_concurrency_gauntlet_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'goroutines_active': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_go_concurrency_gauntlet_scenario([]),
            {'state': {}, 'metrics': {'goroutines_active': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
