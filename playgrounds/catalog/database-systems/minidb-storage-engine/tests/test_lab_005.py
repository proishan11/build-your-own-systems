import unittest

from lab_005 import run_minidb_storage_engine_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_minidb_storage_engine_happy_path_scenario(self):
        self.assertEqual(run_minidb_storage_engine_scenario([{'type': 'apply', 'resource': 'page cache', 'value': 'ready'}, {'type': 'metric', 'name': 'pages_flushed', 'value': 3}, {'type': 'fail', 'reason': 'dirty page loss'}, {'type': 'recover', 'reason': 'dirty page loss'}]), {'state': {'page cache': 'ready'}, 'metrics': {'pages_flushed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_minidb_storage_engine_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'pages_flushed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_minidb_storage_engine_scenario([]),
            {'state': {}, 'metrics': {'pages_flushed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
