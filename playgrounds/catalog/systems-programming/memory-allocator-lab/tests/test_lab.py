import unittest

from lab import split_allocation_heap_allocation


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_heap_allocation_request(self):
        self.assertEqual(split_allocation_heap_allocation({'id': 'heap-allocation-001', 'kind': 'split allocation', 'target': 'free block', 'priority': 2, 'metadata': {'source': 'Memory Allocator Lab', 'track': 'systems-programming'}}), {'id': 'heap-allocation-001', 'action': 'split allocation', 'target': 'free block', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_heap_allocation_request(self):
        self.assertEqual(split_allocation_heap_allocation({'id': 'bad', 'kind': '', 'target': 'free block', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'free block', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'heap-allocation-001', 'kind': 'split allocation', 'target': 'free block', 'priority': 2, 'metadata': {'source': 'Memory Allocator Lab', 'track': 'systems-programming'}}
        original = dict(request)
        split_allocation_heap_allocation(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
