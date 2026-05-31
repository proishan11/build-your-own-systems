import unittest

from lab_004 import recover_rag_from_scratch_lost_citation


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_retrieve_context_failure(self):
        self.assertEqual(recover_rag_from_scratch_lost_citation({'operation': 'retrieve context', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'vector index'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'vector index'})

    def test_fails_permanent_lost_citation(self):
        self.assertEqual(recover_rag_from_scratch_lost_citation({'operation': 'retrieve context', 'error': 'lost citation', 'attempt': 1, 'max_attempts': 3, 'resource': 'vector index'}), {'decision': 'fail', 'reason': 'lost citation', 'resource': 'vector index'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_rag_from_scratch_lost_citation({'operation': 'retrieve context', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'vector index'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'vector index'})


if __name__ == "__main__":
    unittest.main()
