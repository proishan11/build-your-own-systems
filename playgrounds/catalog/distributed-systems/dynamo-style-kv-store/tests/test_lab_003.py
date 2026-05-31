import unittest

from lab_003 import plan_dynamo_style_kv_store_write_quorums


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_write_quorum_operations(self):
        self.assertEqual(plan_dynamo_style_kv_store_write_quorums({'replica-set-primary': 'ready', 'replica-set-canary': 'ready'}, {'replica-set-primary': 'stale', 'replica-set-old': 'ready'}), [{'op': 'update', 'name': 'replica-set-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'replica-set-old', 'from': 'ready'}, {'op': 'create', 'name': 'replica-set-canary', 'to': 'ready'}])

    def test_noops_when_replica_set_already_matches(self):
        current = {'replica-set-primary': 'ready'}
        self.assertEqual(plan_dynamo_style_kv_store_write_quorums(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_dynamo_style_kv_store_write_quorums({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
