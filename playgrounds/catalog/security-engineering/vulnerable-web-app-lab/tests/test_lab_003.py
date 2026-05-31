import unittest

from lab_003 import plan_vulnerable_web_app_lab_sanitize_requests


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_sanitize_request_operations(self):
        self.assertEqual(plan_vulnerable_web_app_lab_sanitize_requests({'security-policy-primary': 'ready', 'security-policy-canary': 'ready'}, {'security-policy-primary': 'stale', 'security-policy-old': 'ready'}), [{'op': 'update', 'name': 'security-policy-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'security-policy-old', 'from': 'ready'}, {'op': 'create', 'name': 'security-policy-canary', 'to': 'ready'}])

    def test_noops_when_security_policy_already_matches(self):
        current = {'security-policy-primary': 'ready'}
        self.assertEqual(plan_vulnerable_web_app_lab_sanitize_requests(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_vulnerable_web_app_lab_sanitize_requests({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
