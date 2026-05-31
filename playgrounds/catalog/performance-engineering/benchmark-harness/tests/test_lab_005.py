import unittest

from lab_005 import run_benchmark_harness_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_benchmark_harness_happy_path_scenario(self):
        self.assertEqual(run_benchmark_harness_scenario([{'type': 'apply', 'resource': 'run config', 'value': 'ready'}, {'type': 'metric', 'name': 'confidence_interval', 'value': 3}, {'type': 'fail', 'reason': 'warmup bias'}, {'type': 'recover', 'reason': 'warmup bias'}]), {'state': {'run config': 'ready'}, 'metrics': {'confidence_interval': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_benchmark_harness_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'confidence_interval': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_benchmark_harness_scenario([]),
            {'state': {}, 'metrics': {'confidence_interval': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
