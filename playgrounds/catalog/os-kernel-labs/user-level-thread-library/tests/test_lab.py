import unittest

from lab import yield_thread_green_thread


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_green_thread_request(self):
        self.assertEqual(yield_thread_green_thread({'id': 'green-thread-001', 'kind': 'yield thread', 'target': 'run queue', 'priority': 2, 'metadata': {'source': 'User-Level Thread Library', 'track': 'os-kernel-labs'}}), {'id': 'green-thread-001', 'action': 'yield thread', 'target': 'run queue', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_green_thread_request(self):
        self.assertEqual(yield_thread_green_thread({'id': 'bad', 'kind': '', 'target': 'run queue', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'run queue', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'green-thread-001', 'kind': 'yield thread', 'target': 'run queue', 'priority': 2, 'metadata': {'source': 'User-Level Thread Library', 'track': 'os-kernel-labs'}}
        original = dict(request)
        yield_thread_green_thread(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
