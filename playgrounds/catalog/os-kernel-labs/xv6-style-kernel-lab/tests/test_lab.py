import unittest

from lab import enter_kernel_system_call


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_system_call_request(self):
        self.assertEqual(enter_kernel_system_call({'id': 'system-call-001', 'kind': 'enter kernel', 'target': 'process table', 'priority': 2, 'metadata': {'source': 'xv6-Style Kernel Lab', 'track': 'os-kernel-labs'}}), {'id': 'system-call-001', 'action': 'enter kernel', 'target': 'process table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_system_call_request(self):
        self.assertEqual(enter_kernel_system_call({'id': 'bad', 'kind': '', 'target': 'process table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'process table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'system-call-001', 'kind': 'enter kernel', 'target': 'process table', 'priority': 2, 'metadata': {'source': 'xv6-Style Kernel Lab', 'track': 'os-kernel-labs'}}
        original = dict(request)
        enter_kernel_system_call(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
