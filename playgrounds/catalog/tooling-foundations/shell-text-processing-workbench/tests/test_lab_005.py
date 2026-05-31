import unittest

from lab_005 import run_shell_text_processing_workbench_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_shell_text_processing_workbench_happy_path_scenario(self):
        self.assertEqual(run_shell_text_processing_workbench_scenario([{'type': 'apply', 'resource': 'pipeline stage', 'value': 'ready'}, {'type': 'metric', 'name': 'records_processed', 'value': 3}, {'type': 'fail', 'reason': 'locale mismatch'}, {'type': 'recover', 'reason': 'locale mismatch'}]), {'state': {'pipeline stage': 'ready'}, 'metrics': {'records_processed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_shell_text_processing_workbench_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'records_processed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_shell_text_processing_workbench_scenario([]),
            {'state': {}, 'metrics': {'records_processed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
