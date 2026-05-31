import unittest

from lab_005 import run_operator_for_postgresql_backups_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_operator_for_postgresql_backups_happy_path_scenario(self):
        self.assertEqual(run_operator_for_postgresql_backups_scenario([{'type': 'apply', 'resource': 'backup schedule', 'value': 'ready'}, {'type': 'metric', 'name': 'backups_completed', 'value': 3}, {'type': 'fail', 'reason': 'missing wal archive'}, {'type': 'recover', 'reason': 'missing wal archive'}]), {'state': {'backup schedule': 'ready'}, 'metrics': {'backups_completed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_operator_for_postgresql_backups_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'backups_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_operator_for_postgresql_backups_scenario([]),
            {'state': {}, 'metrics': {'backups_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
