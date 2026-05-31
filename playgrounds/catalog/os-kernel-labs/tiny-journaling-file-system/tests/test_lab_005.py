import unittest

from lab_005 import run_tiny_journaling_file_system_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_tiny_journaling_file_system_happy_path_scenario(self):
        self.assertEqual(run_tiny_journaling_file_system_scenario([{'type': 'apply', 'resource': 'inode block', 'value': 'ready'}, {'type': 'metric', 'name': 'replayed_transactions', 'value': 3}, {'type': 'fail', 'reason': 'torn journal write'}, {'type': 'recover', 'reason': 'torn journal write'}]), {'state': {'inode block': 'ready'}, 'metrics': {'replayed_transactions': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_tiny_journaling_file_system_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'replayed_transactions': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_tiny_journaling_file_system_scenario([]),
            {'state': {}, 'metrics': {'replayed_transactions': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
