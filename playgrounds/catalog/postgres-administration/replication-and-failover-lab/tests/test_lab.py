import unittest

from lab import promote_replica_replica_status


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_replica_status_request(self):
        self.assertEqual(promote_replica_replica_status({'id': 'replica-status-001', 'kind': 'promote replica', 'target': 'failover plan', 'priority': 2, 'metadata': {'source': 'Replication and Failover Lab', 'track': 'postgres-administration'}}), {'id': 'replica-status-001', 'action': 'promote replica', 'target': 'failover plan', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_replica_status_request(self):
        self.assertEqual(promote_replica_replica_status({'id': 'bad', 'kind': '', 'target': 'failover plan', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'failover plan', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'replica-status-001', 'kind': 'promote replica', 'target': 'failover plan', 'priority': 2, 'metadata': {'source': 'Replication and Failover Lab', 'track': 'postgres-administration'}}
        original = dict(request)
        promote_replica_replica_status(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
