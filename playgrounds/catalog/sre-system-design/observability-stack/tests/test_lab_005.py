import unittest

from lab_005 import run_observability_stack_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_observability_stack_happy_path_scenario(self):
        self.assertEqual(run_observability_stack_scenario([{'type': 'apply', 'resource': 'signal pipeline', 'value': 'ready'}, {'type': 'metric', 'name': 'spans_ingested', 'value': 3}, {'type': 'fail', 'reason': 'cardinality explosion'}, {'type': 'recover', 'reason': 'cardinality explosion'}]), {'state': {'signal pipeline': 'ready'}, 'metrics': {'spans_ingested': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_observability_stack_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'spans_ingested': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_observability_stack_scenario([]),
            {'state': {}, 'metrics': {'spans_ingested': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
