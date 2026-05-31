import unittest

from lab_005 import run_http_server_from_scratch_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_http_server_from_scratch_happy_path_scenario(self):
        self.assertEqual(run_http_server_from_scratch_scenario([{'type': 'apply', 'resource': 'route table', 'value': 'ready'}, {'type': 'metric', 'name': 'responses_sent', 'value': 3}, {'type': 'fail', 'reason': 'malformed header'}, {'type': 'recover', 'reason': 'malformed header'}]), {'state': {'route table': 'ready'}, 'metrics': {'responses_sent': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_http_server_from_scratch_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'responses_sent': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_http_server_from_scratch_scenario([]),
            {'state': {}, 'metrics': {'responses_sent': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
