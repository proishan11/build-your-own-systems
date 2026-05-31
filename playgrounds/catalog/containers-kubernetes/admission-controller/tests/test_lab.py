import unittest

from lab import admit_object_admission_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_admission_request_request(self):
        self.assertEqual(admit_object_admission_request({'id': 'admission-request-001', 'kind': 'admit object', 'target': 'policy set', 'priority': 2, 'metadata': {'source': 'Admission Controller', 'track': 'containers-kubernetes'}}), {'id': 'admission-request-001', 'action': 'admit object', 'target': 'policy set', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_admission_request_request(self):
        self.assertEqual(admit_object_admission_request({'id': 'bad', 'kind': '', 'target': 'policy set', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'policy set', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'admission-request-001', 'kind': 'admit object', 'target': 'policy set', 'priority': 2, 'metadata': {'source': 'Admission Controller', 'track': 'containers-kubernetes'}}
        original = dict(request)
        admit_object_admission_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
