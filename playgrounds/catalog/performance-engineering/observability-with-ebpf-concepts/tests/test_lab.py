import unittest

from lab import attach_probe_kernel_event


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_kernel_event_request(self):
        self.assertEqual(attach_probe_kernel_event({'id': 'kernel-event-001', 'kind': 'attach probe', 'target': 'probe registry', 'priority': 2, 'metadata': {'source': 'Observability With eBPF Concepts', 'track': 'performance-engineering'}}), {'id': 'kernel-event-001', 'action': 'attach probe', 'target': 'probe registry', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_kernel_event_request(self):
        self.assertEqual(attach_probe_kernel_event({'id': 'bad', 'kind': '', 'target': 'probe registry', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'probe registry', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'kernel-event-001', 'kind': 'attach probe', 'target': 'probe registry', 'priority': 2, 'metadata': {'source': 'Observability With eBPF Concepts', 'track': 'performance-engineering'}}
        original = dict(request)
        attach_probe_kernel_event(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
