import unittest

from lab import rotate_secret_secret_version


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_secret_version_request(self):
        self.assertEqual(rotate_secret_secret_version({'id': 'secret-version-001', 'kind': 'rotate secret', 'target': 'secret store', 'priority': 2, 'metadata': {'source': 'Secrets Manager', 'track': 'security-engineering'}}), {'id': 'secret-version-001', 'action': 'rotate secret', 'target': 'secret store', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_secret_version_request(self):
        self.assertEqual(rotate_secret_secret_version({'id': 'bad', 'kind': '', 'target': 'secret store', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'secret store', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'secret-version-001', 'kind': 'rotate secret', 'target': 'secret store', 'priority': 2, 'metadata': {'source': 'Secrets Manager', 'track': 'security-engineering'}}
        original = dict(request)
        rotate_secret_secret_version(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
