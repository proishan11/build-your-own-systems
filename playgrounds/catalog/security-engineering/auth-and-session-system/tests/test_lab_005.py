import unittest

from lab_005 import run_auth_and_session_system_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_auth_and_session_system_happy_path_scenario(self):
        self.assertEqual(run_auth_and_session_system_scenario([{'type': 'apply', 'resource': 'session store', 'value': 'ready'}, {'type': 'metric', 'name': 'sessions_revoked', 'value': 3}, {'type': 'fail', 'reason': 'session fixation'}, {'type': 'recover', 'reason': 'session fixation'}]), {'state': {'session store': 'ready'}, 'metrics': {'sessions_revoked': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_auth_and_session_system_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'sessions_revoked': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_auth_and_session_system_scenario([]),
            {'state': {}, 'metrics': {'sessions_revoked': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
