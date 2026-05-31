import unittest

from lab_005 import run_lock_contention_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_lock_contention_lab_happy_path_scenario(self):
        self.assertEqual(run_lock_contention_lab_scenario([{'type': 'apply', 'resource': 'wait graph', 'value': 'ready'}, {'type': 'metric', 'name': 'wait_time_ms', 'value': 3}, {'type': 'fail', 'reason': 'convoy effect'}, {'type': 'recover', 'reason': 'convoy effect'}]), {'state': {'wait graph': 'ready'}, 'metrics': {'wait_time_ms': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_lock_contention_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'wait_time_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_lock_contention_lab_scenario([]),
            {'state': {}, 'metrics': {'wait_time_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
