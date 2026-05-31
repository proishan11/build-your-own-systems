import unittest

from lab import write_quorum_kv_write


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_kv_write_request(self):
        self.assertEqual(write_quorum_kv_write({'id': 'kv-write-001', 'kind': 'write quorum', 'target': 'replica set', 'priority': 2, 'metadata': {'source': 'Dynamo-Style KV Store', 'track': 'distributed-systems'}}), {'id': 'kv-write-001', 'action': 'write quorum', 'target': 'replica set', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_kv_write_request(self):
        self.assertEqual(write_quorum_kv_write({'id': 'bad', 'kind': '', 'target': 'replica set', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'replica set', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'kv-write-001', 'kind': 'write quorum', 'target': 'replica set', 'priority': 2, 'metadata': {'source': 'Dynamo-Style KV Store', 'track': 'distributed-systems'}}
        original = dict(request)
        write_quorum_kv_write(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
