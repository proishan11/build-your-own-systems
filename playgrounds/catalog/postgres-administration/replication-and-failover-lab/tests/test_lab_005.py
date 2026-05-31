import unittest

from lab_005 import run_replication_and_failover_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_replication_and_failover_lab_happy_path_scenario(self):
        self.assertEqual(run_replication_and_failover_lab_scenario([{'type': 'apply', 'resource': 'failover plan', 'value': 'ready'}, {'type': 'metric', 'name': 'replicas_healthy', 'value': 3}, {'type': 'fail', 'reason': 'split brain'}, {'type': 'recover', 'reason': 'split brain'}]), {'state': {'failover plan': 'ready'}, 'metrics': {'replicas_healthy': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_replication_and_failover_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'replicas_healthy': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_replication_and_failover_lab_scenario([]),
            {'state': {}, 'metrics': {'replicas_healthy': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
