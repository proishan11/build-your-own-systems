import unittest

from lab import fan_out_work_concurrent_job


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_concurrent_job_request(self):
        self.assertEqual(fan_out_work_concurrent_job({'id': 'concurrent-job-001', 'kind': 'fan out work', 'target': 'worker group', 'priority': 2, 'metadata': {'source': 'Go Concurrency Gauntlet', 'track': 'go-concurrency'}}), {'id': 'concurrent-job-001', 'action': 'fan out work', 'target': 'worker group', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_concurrent_job_request(self):
        self.assertEqual(fan_out_work_concurrent_job({'id': 'bad', 'kind': '', 'target': 'worker group', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'worker group', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'concurrent-job-001', 'kind': 'fan out work', 'target': 'worker group', 'priority': 2, 'metadata': {'source': 'Go Concurrency Gauntlet', 'track': 'go-concurrency'}}
        original = dict(request)
        fan_out_work_concurrent_job(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
