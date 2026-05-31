import unittest

from lab_005 import run_dynamo_style_kv_store_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_dynamo_style_kv_store_happy_path_scenario(self):
        self.assertEqual(run_dynamo_style_kv_store_scenario([{'type': 'apply', 'resource': 'replica set', 'value': 'ready'}, {'type': 'metric', 'name': 'vector_clock_entries', 'value': 3}, {'type': 'fail', 'reason': 'sibling conflict'}, {'type': 'recover', 'reason': 'sibling conflict'}]), {'state': {'replica set': 'ready'}, 'metrics': {'vector_clock_entries': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_dynamo_style_kv_store_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'vector_clock_entries': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_dynamo_style_kv_store_scenario([]),
            {'state': {}, 'metrics': {'vector_clock_entries': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
