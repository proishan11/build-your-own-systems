import unittest

from lab_005 import run_dns_resolver_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_dns_resolver_happy_path_scenario(self):
        self.assertEqual(run_dns_resolver_scenario([{'type': 'apply', 'resource': 'resolver cache', 'value': 'ready'}, {'type': 'metric', 'name': 'cache_hits', 'value': 3}, {'type': 'fail', 'reason': 'ttl expiry'}, {'type': 'recover', 'reason': 'ttl expiry'}]), {'state': {'resolver cache': 'ready'}, 'metrics': {'cache_hits': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_dns_resolver_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'cache_hits': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_dns_resolver_scenario([]),
            {'state': {}, 'metrics': {'cache_hits': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
