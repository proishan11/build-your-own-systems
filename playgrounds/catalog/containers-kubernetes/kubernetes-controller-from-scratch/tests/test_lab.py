import unittest

from lab import reconcile_object_custom_resource


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_custom_resource_request(self):
        self.assertEqual(reconcile_object_custom_resource({'id': 'custom-resource-001', 'kind': 'reconcile object', 'target': 'reconcile state', 'priority': 2, 'metadata': {'source': 'Kubernetes Controller From Scratch', 'track': 'containers-kubernetes'}}), {'id': 'custom-resource-001', 'action': 'reconcile object', 'target': 'reconcile state', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_custom_resource_request(self):
        self.assertEqual(reconcile_object_custom_resource({'id': 'bad', 'kind': '', 'target': 'reconcile state', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'reconcile state', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'custom-resource-001', 'kind': 'reconcile object', 'target': 'reconcile state', 'priority': 2, 'metadata': {'source': 'Kubernetes Controller From Scratch', 'track': 'containers-kubernetes'}}
        original = dict(request)
        reconcile_object_custom_resource(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
