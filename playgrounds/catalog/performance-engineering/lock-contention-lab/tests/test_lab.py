import unittest

from lab import attribute_wait_lock_event


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_lock_event_request(self):
        self.assertEqual(attribute_wait_lock_event({'id': 'lock-event-001', 'kind': 'attribute wait', 'target': 'wait graph', 'priority': 2, 'metadata': {'source': 'Lock Contention Lab', 'track': 'performance-engineering'}}), {'id': 'lock-event-001', 'action': 'attribute wait', 'target': 'wait graph', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_lock_event_request(self):
        self.assertEqual(attribute_wait_lock_event({'id': 'bad', 'kind': '', 'target': 'wait graph', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'wait graph', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'lock-event-001', 'kind': 'attribute wait', 'target': 'wait graph', 'priority': 2, 'metadata': {'source': 'Lock Contention Lab', 'track': 'performance-engineering'}}
        original = dict(request)
        attribute_wait_lock_event(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
