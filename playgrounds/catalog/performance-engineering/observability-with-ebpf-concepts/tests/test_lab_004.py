import unittest

from lab_004 import recover_observability_with_ebpf_concepts_unsafe_probe


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_attach_probe_failure(self):
        self.assertEqual(recover_observability_with_ebpf_concepts_unsafe_probe({'operation': 'attach probe', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'probe registry'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'probe registry'})

    def test_fails_permanent_unsafe_probe(self):
        self.assertEqual(recover_observability_with_ebpf_concepts_unsafe_probe({'operation': 'attach probe', 'error': 'unsafe probe', 'attempt': 1, 'max_attempts': 3, 'resource': 'probe registry'}), {'decision': 'fail', 'reason': 'unsafe probe', 'resource': 'probe registry'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_observability_with_ebpf_concepts_unsafe_probe({'operation': 'attach probe', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'probe registry'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'probe registry'})


if __name__ == "__main__":
    unittest.main()
