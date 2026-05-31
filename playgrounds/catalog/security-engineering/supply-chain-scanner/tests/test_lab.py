import unittest

from lab import scan_artifact_package_artifact


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_package_artifact_request(self):
        self.assertEqual(scan_artifact_package_artifact({'id': 'package-artifact-001', 'kind': 'scan artifact', 'target': 'sbom index', 'priority': 2, 'metadata': {'source': 'Supply-Chain Scanner', 'track': 'security-engineering'}}), {'id': 'package-artifact-001', 'action': 'scan artifact', 'target': 'sbom index', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_package_artifact_request(self):
        self.assertEqual(scan_artifact_package_artifact({'id': 'bad', 'kind': '', 'target': 'sbom index', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'sbom index', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'package-artifact-001', 'kind': 'scan artifact', 'target': 'sbom index', 'priority': 2, 'metadata': {'source': 'Supply-Chain Scanner', 'track': 'security-engineering'}}
        original = dict(request)
        scan_artifact_package_artifact(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
