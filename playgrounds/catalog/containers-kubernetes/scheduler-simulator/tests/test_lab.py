import unittest

from lab import bind_pod_pod_placement


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_pod_placement_request(self):
        self.assertEqual(bind_pod_pod_placement({'id': 'pod-placement-001', 'kind': 'bind pod', 'target': 'node inventory', 'priority': 2, 'metadata': {'source': 'Scheduler Simulator', 'track': 'containers-kubernetes'}}), {'id': 'pod-placement-001', 'action': 'bind pod', 'target': 'node inventory', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_pod_placement_request(self):
        self.assertEqual(bind_pod_pod_placement({'id': 'bad', 'kind': '', 'target': 'node inventory', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'node inventory', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'pod-placement-001', 'kind': 'bind pod', 'target': 'node inventory', 'priority': 2, 'metadata': {'source': 'Scheduler Simulator', 'track': 'containers-kubernetes'}}
        original = dict(request)
        bind_pod_pod_placement(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
