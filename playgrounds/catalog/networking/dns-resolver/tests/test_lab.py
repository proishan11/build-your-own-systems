import unittest

from lab import resolve_record_dns_question


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_dns_question_request(self):
        self.assertEqual(resolve_record_dns_question({'id': 'dns-question-001', 'kind': 'resolve record', 'target': 'resolver cache', 'priority': 2, 'metadata': {'source': 'DNS Resolver', 'track': 'networking'}}), {'id': 'dns-question-001', 'action': 'resolve record', 'target': 'resolver cache', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_dns_question_request(self):
        self.assertEqual(resolve_record_dns_question({'id': 'bad', 'kind': '', 'target': 'resolver cache', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'resolver cache', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'dns-question-001', 'kind': 'resolve record', 'target': 'resolver cache', 'priority': 2, 'metadata': {'source': 'DNS Resolver', 'track': 'networking'}}
        original = dict(request)
        resolve_record_dns_question(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
