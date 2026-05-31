import unittest

from lab import filter_record_text_record


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_text_record_request(self):
        self.assertEqual(filter_record_text_record({'id': 'text-record-001', 'kind': 'filter record', 'target': 'pipeline stage', 'priority': 2, 'metadata': {'source': 'Shell Text Processing Workbench', 'track': 'tooling-foundations'}}), {'id': 'text-record-001', 'action': 'filter record', 'target': 'pipeline stage', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_text_record_request(self):
        self.assertEqual(filter_record_text_record({'id': 'bad', 'kind': '', 'target': 'pipeline stage', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'pipeline stage', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'text-record-001', 'kind': 'filter record', 'target': 'pipeline stage', 'priority': 2, 'metadata': {'source': 'Shell Text Processing Workbench', 'track': 'tooling-foundations'}}
        original = dict(request)
        filter_record_text_record(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
