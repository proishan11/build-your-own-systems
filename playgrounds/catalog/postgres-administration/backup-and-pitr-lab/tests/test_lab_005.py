import unittest

from lab_005 import run_backup_and_pitr_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_backup_and_pitr_lab_happy_path_scenario(self):
        self.assertEqual(run_backup_and_pitr_lab_scenario([{'type': 'apply', 'resource': 'backup catalog', 'value': 'ready'}, {'type': 'metric', 'name': 'segments_restored', 'value': 3}, {'type': 'fail', 'reason': 'missing base backup'}, {'type': 'recover', 'reason': 'missing base backup'}]), {'state': {'backup catalog': 'ready'}, 'metrics': {'segments_restored': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_backup_and_pitr_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'segments_restored': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_backup_and_pitr_lab_scenario([]),
            {'state': {}, 'metrics': {'segments_restored': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
