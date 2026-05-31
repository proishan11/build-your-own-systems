import unittest

from lab_005 import run_mapreduce_runtime_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_mapreduce_runtime_happy_path_scenario(self):
        self.assertEqual(run_mapreduce_runtime_scenario([{'type': 'apply', 'resource': 'task tracker', 'value': 'ready'}, {'type': 'metric', 'name': 'tasks_completed', 'value': 3}, {'type': 'fail', 'reason': 'worker crash'}, {'type': 'recover', 'reason': 'worker crash'}]), {'state': {'task tracker': 'ready'}, 'metrics': {'tasks_completed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_mapreduce_runtime_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'tasks_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_mapreduce_runtime_scenario([]),
            {'state': {}, 'metrics': {'tasks_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
