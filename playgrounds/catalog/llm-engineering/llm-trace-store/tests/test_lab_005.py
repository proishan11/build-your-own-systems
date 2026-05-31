import unittest

from lab_005 import run_llm_trace_store_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_llm_trace_store_happy_path_scenario(self):
        self.assertEqual(run_llm_trace_store_scenario([{'type': 'apply', 'resource': 'trace index', 'value': 'ready'}, {'type': 'metric', 'name': 'traces_indexed', 'value': 3}, {'type': 'fail', 'reason': 'missing parent span'}, {'type': 'recover', 'reason': 'missing parent span'}]), {'state': {'trace index': 'ready'}, 'metrics': {'traces_indexed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_llm_trace_store_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'traces_indexed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_llm_trace_store_scenario([]),
            {'state': {}, 'metrics': {'traces_indexed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
