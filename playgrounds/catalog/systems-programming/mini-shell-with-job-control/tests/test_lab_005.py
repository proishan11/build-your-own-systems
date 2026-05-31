import unittest

from lab_005 import run_mini_shell_with_job_control_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_mini_shell_with_job_control_happy_path_scenario(self):
        self.assertEqual(run_mini_shell_with_job_control_scenario([{'type': 'apply', 'resource': 'process group', 'value': 'ready'}, {'type': 'metric', 'name': 'foreground_jobs', 'value': 3}, {'type': 'fail', 'reason': 'orphaned background job'}, {'type': 'recover', 'reason': 'orphaned background job'}]), {'state': {'process group': 'ready'}, 'metrics': {'foreground_jobs': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_mini_shell_with_job_control_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'foreground_jobs': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_mini_shell_with_job_control_scenario([]),
            {'state': {}, 'metrics': {'foreground_jobs': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
