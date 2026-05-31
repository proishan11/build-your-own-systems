import unittest

from lab_005 import run_human_approval_workflow_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_human_approval_workflow_happy_path_scenario(self):
        self.assertEqual(run_human_approval_workflow_scenario([{'type': 'apply', 'resource': 'approval queue', 'value': 'ready'}, {'type': 'metric', 'name': 'approvals_resolved', 'value': 3}, {'type': 'fail', 'reason': 'stale approval'}, {'type': 'recover', 'reason': 'stale approval'}]), {'state': {'approval queue': 'ready'}, 'metrics': {'approvals_resolved': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_human_approval_workflow_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'approvals_resolved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_human_approval_workflow_scenario([]),
            {'state': {}, 'metrics': {'approvals_resolved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
