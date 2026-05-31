import unittest

from lab_003 import plan_auth_and_session_system_authenticate_sessions


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_authenticate_session_operations(self):
        self.assertEqual(plan_auth_and_session_system_authenticate_sessions({'session-store-primary': 'ready', 'session-store-canary': 'ready'}, {'session-store-primary': 'stale', 'session-store-old': 'ready'}), [{'op': 'update', 'name': 'session-store-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'session-store-old', 'from': 'ready'}, {'op': 'create', 'name': 'session-store-canary', 'to': 'ready'}])

    def test_noops_when_session_store_already_matches(self):
        current = {'session-store-primary': 'ready'}
        self.assertEqual(plan_auth_and_session_system_authenticate_sessions(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_auth_and_session_system_authenticate_sessions({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
