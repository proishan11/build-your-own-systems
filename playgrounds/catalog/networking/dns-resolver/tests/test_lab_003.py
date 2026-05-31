import unittest

from lab_003 import plan_dns_resolver_resolve_records


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_resolve_record_operations(self):
        self.assertEqual(plan_dns_resolver_resolve_records({'resolver-cache-primary': 'ready', 'resolver-cache-canary': 'ready'}, {'resolver-cache-primary': 'stale', 'resolver-cache-old': 'ready'}), [{'op': 'update', 'name': 'resolver-cache-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'resolver-cache-old', 'from': 'ready'}, {'op': 'create', 'name': 'resolver-cache-canary', 'to': 'ready'}])

    def test_noops_when_resolver_cache_already_matches(self):
        current = {'resolver-cache-primary': 'ready'}
        self.assertEqual(plan_dns_resolver_resolve_records(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_dns_resolver_resolve_records({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
