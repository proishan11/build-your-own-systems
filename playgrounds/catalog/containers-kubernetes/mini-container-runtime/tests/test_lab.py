import unittest

from lab import start_container_container_spec


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_container_spec_request(self):
        self.assertEqual(start_container_container_spec({'id': 'container-spec-001', 'kind': 'start container', 'target': 'namespace plan', 'priority': 2, 'metadata': {'source': 'Mini Container Runtime', 'track': 'containers-kubernetes'}}), {'id': 'container-spec-001', 'action': 'start container', 'target': 'namespace plan', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_container_spec_request(self):
        self.assertEqual(start_container_container_spec({'id': 'bad', 'kind': '', 'target': 'namespace plan', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'namespace plan', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'container-spec-001', 'kind': 'start container', 'target': 'namespace plan', 'priority': 2, 'metadata': {'source': 'Mini Container Runtime', 'track': 'containers-kubernetes'}}
        original = dict(request)
        start_container_container_spec(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
