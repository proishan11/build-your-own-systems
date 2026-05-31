import unittest

from lab_005 import run_rate_limited_api_gateway_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_rate_limited_api_gateway_happy_path_scenario(self):
        self.assertEqual(run_rate_limited_api_gateway_scenario([{'type': 'apply', 'resource': 'token bucket', 'value': 'ready'}, {'type': 'metric', 'name': 'requests_allowed', 'value': 3}, {'type': 'fail', 'reason': 'limit bypass'}, {'type': 'recover', 'reason': 'limit bypass'}]), {'state': {'token bucket': 'ready'}, 'metrics': {'requests_allowed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_rate_limited_api_gateway_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'requests_allowed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_rate_limited_api_gateway_scenario([]),
            {'state': {}, 'metrics': {'requests_allowed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
