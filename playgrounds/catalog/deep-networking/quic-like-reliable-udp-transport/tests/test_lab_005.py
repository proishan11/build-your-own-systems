import unittest

from lab_005 import run_quic_like_reliable_udp_transport_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_quic_like_reliable_udp_transport_happy_path_scenario(self):
        self.assertEqual(run_quic_like_reliable_udp_transport_scenario([{'type': 'apply', 'resource': 'connection state', 'value': 'ready'}, {'type': 'metric', 'name': 'streams_open', 'value': 3}, {'type': 'fail', 'reason': 'lost packet'}, {'type': 'recover', 'reason': 'lost packet'}]), {'state': {'connection state': 'ready'}, 'metrics': {'streams_open': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_quic_like_reliable_udp_transport_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'streams_open': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_quic_like_reliable_udp_transport_scenario([]),
            {'state': {}, 'metrics': {'streams_open': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
