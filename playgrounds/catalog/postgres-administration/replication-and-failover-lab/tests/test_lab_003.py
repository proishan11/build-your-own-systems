import unittest

from lab_003 import plan_replication_and_failover_lab_promote_replicas


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_promote_replica_operations(self):
        self.assertEqual(plan_replication_and_failover_lab_promote_replicas({'failover-plan-primary': 'ready', 'failover-plan-canary': 'ready'}, {'failover-plan-primary': 'stale', 'failover-plan-old': 'ready'}), [{'op': 'update', 'name': 'failover-plan-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'failover-plan-old', 'from': 'ready'}, {'op': 'create', 'name': 'failover-plan-canary', 'to': 'ready'}])

    def test_noops_when_failover_plan_already_matches(self):
        current = {'failover-plan-primary': 'ready'}
        self.assertEqual(plan_replication_and_failover_lab_promote_replicas(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_replication_and_failover_lab_promote_replicas({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
