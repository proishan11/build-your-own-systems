import unittest

from lab_005 import run_replicated_wal_with_raft_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_replicated_wal_with_raft_happy_path_scenario(self):
        self.assertEqual(run_replicated_wal_with_raft_scenario([{'type': 'apply', 'resource': 'replica log', 'value': 'ready'}, {'type': 'metric', 'name': 'commit_index', 'value': 3}, {'type': 'fail', 'reason': 'term mismatch'}, {'type': 'recover', 'reason': 'term mismatch'}]), {'state': {'replica log': 'ready'}, 'metrics': {'commit_index': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_replicated_wal_with_raft_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'commit_index': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_replicated_wal_with_raft_scenario([]),
            {'state': {}, 'metrics': {'commit_index': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
