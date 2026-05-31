import unittest

from lab import relax_route_route_advertisement


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_route_advertisement_request(self):
        self.assertEqual(relax_route_route_advertisement({'id': 'route-advertisement-001', 'kind': 'relax route', 'target': 'neighbor table', 'priority': 2, 'metadata': {'source': 'Dynamic Routing Simulator', 'track': 'deep-networking'}}), {'id': 'route-advertisement-001', 'action': 'relax route', 'target': 'neighbor table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_route_advertisement_request(self):
        self.assertEqual(relax_route_route_advertisement({'id': 'bad', 'kind': '', 'target': 'neighbor table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'neighbor table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'route-advertisement-001', 'kind': 'relax route', 'target': 'neighbor table', 'priority': 2, 'metadata': {'source': 'Dynamic Routing Simulator', 'track': 'deep-networking'}}
        original = dict(request)
        relax_route_route_advertisement(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
