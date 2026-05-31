import unittest

from lab_005 import run_ip_router_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_ip_router_lab_happy_path_scenario(self):
        self.assertEqual(run_ip_router_lab_scenario([{'type': 'apply', 'resource': 'routing table', 'value': 'ready'}, {'type': 'metric', 'name': 'packets_forwarded', 'value': 3}, {'type': 'fail', 'reason': 'ttl expired'}, {'type': 'recover', 'reason': 'ttl expired'}]), {'state': {'routing table': 'ready'}, 'metrics': {'packets_forwarded': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_ip_router_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'packets_forwarded': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_ip_router_lab_scenario([]),
            {'state': {}, 'metrics': {'packets_forwarded': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
