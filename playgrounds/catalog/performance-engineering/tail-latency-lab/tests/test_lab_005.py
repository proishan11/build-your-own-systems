import unittest

from lab_005 import run_tail_latency_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_tail_latency_lab_happy_path_scenario(self):
        self.assertEqual(run_tail_latency_lab_scenario([{'type': 'apply', 'resource': 'histogram bucket', 'value': 'ready'}, {'type': 'metric', 'name': 'p99_latency_ms', 'value': 3}, {'type': 'fail', 'reason': 'coordinated omission'}, {'type': 'recover', 'reason': 'coordinated omission'}]), {'state': {'histogram bucket': 'ready'}, 'metrics': {'p99_latency_ms': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_tail_latency_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'p99_latency_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_tail_latency_lab_scenario([]),
            {'state': {}, 'metrics': {'p99_latency_ms': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
