import unittest

from lab_005 import run_cost_and_latency_dashboard_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_cost_and_latency_dashboard_happy_path_scenario(self):
        self.assertEqual(run_cost_and_latency_dashboard_scenario([{'type': 'apply', 'resource': 'metric bucket', 'value': 'ready'}, {'type': 'metric', 'name': 'p95_latency_ms', 'value': 3}, {'type': 'fail', 'reason': 'tail spike'}, {'type': 'recover', 'reason': 'tail spike'}]), {'state': {'metric bucket': 'ready'}, 'metrics': {'p95_latency_ms': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_cost_and_latency_dashboard_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'p95_latency_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_cost_and_latency_dashboard_scenario([]),
            {'state': {}, 'metrics': {'p95_latency_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
