import unittest

from lab import map_page_virtual_page


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_virtual_page_request(self):
        self.assertEqual(map_page_virtual_page({'id': 'virtual-page-001', 'kind': 'map page', 'target': 'page table', 'priority': 2, 'metadata': {'source': 'Virtual Memory Simulator', 'track': 'os-kernel-labs'}}), {'id': 'virtual-page-001', 'action': 'map page', 'target': 'page table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_virtual_page_request(self):
        self.assertEqual(map_page_virtual_page({'id': 'bad', 'kind': '', 'target': 'page table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'page table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'virtual-page-001', 'kind': 'map page', 'target': 'page table', 'priority': 2, 'metadata': {'source': 'Virtual Memory Simulator', 'track': 'os-kernel-labs'}}
        original = dict(request)
        map_page_virtual_page(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
