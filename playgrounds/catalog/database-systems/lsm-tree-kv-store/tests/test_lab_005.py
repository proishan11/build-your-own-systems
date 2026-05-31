import unittest

from lab_005 import run_lsm_tree_kv_store_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_lsm_tree_kv_store_happy_path_scenario(self):
        self.assertEqual(run_lsm_tree_kv_store_scenario([{'type': 'apply', 'resource': 'sstable level', 'value': 'ready'}, {'type': 'metric', 'name': 'compactions_run', 'value': 3}, {'type': 'fail', 'reason': 'tombstone resurrection'}, {'type': 'recover', 'reason': 'tombstone resurrection'}]), {'state': {'sstable level': 'ready'}, 'metrics': {'compactions_run': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_lsm_tree_kv_store_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'compactions_run': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_lsm_tree_kv_store_scenario([]),
            {'state': {}, 'metrics': {'compactions_run': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
