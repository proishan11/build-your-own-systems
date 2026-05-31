import unittest

from lab_005 import run_user_level_thread_library_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_user_level_thread_library_happy_path_scenario(self):
        self.assertEqual(run_user_level_thread_library_scenario([{'type': 'apply', 'resource': 'run queue', 'value': 'ready'}, {'type': 'metric', 'name': 'context_switches', 'value': 3}, {'type': 'fail', 'reason': 'lost wakeup'}, {'type': 'recover', 'reason': 'lost wakeup'}]), {'state': {'run queue': 'ready'}, 'metrics': {'context_switches': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_user_level_thread_library_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'context_switches': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_user_level_thread_library_scenario([]),
            {'state': {}, 'metrics': {'context_switches': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
