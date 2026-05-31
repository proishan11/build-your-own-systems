import unittest

from lab_003 import plan_replicated_wal_with_raft_append_entriess


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_append_entries_operations(self):
        self.assertEqual(plan_replicated_wal_with_raft_append_entriess({'replica-log-primary': 'ready', 'replica-log-canary': 'ready'}, {'replica-log-primary': 'stale', 'replica-log-old': 'ready'}), [{'op': 'update', 'name': 'replica-log-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'replica-log-old', 'from': 'ready'}, {'op': 'create', 'name': 'replica-log-canary', 'to': 'ready'}])

    def test_noops_when_replica_log_already_matches(self):
        current = {'replica-log-primary': 'ready'}
        self.assertEqual(plan_replicated_wal_with_raft_append_entriess(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_replicated_wal_with_raft_append_entriess({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
