import unittest

from lab_005 import run_scheduler_simulator_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_scheduler_simulator_happy_path_scenario(self):
        self.assertEqual(run_scheduler_simulator_scenario([{'type': 'apply', 'resource': 'node inventory', 'value': 'ready'}, {'type': 'metric', 'name': 'pods_scheduled', 'value': 3}, {'type': 'fail', 'reason': 'resource overcommit'}, {'type': 'recover', 'reason': 'resource overcommit'}]), {'state': {'node inventory': 'ready'}, 'metrics': {'pods_scheduled': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_scheduler_simulator_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'pods_scheduled': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_scheduler_simulator_scenario([]),
            {'state': {}, 'metrics': {'pods_scheduled': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
