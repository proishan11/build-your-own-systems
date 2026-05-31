import unittest

from lab_004 import recover_graphrag_knowledge_system_duplicate_entity


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_link_entity_failure(self):
        self.assertEqual(recover_graphrag_knowledge_system_duplicate_entity({'operation': 'link entity', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'knowledge graph'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'knowledge graph'})

    def test_fails_permanent_duplicate_entity(self):
        self.assertEqual(recover_graphrag_knowledge_system_duplicate_entity({'operation': 'link entity', 'error': 'duplicate entity', 'attempt': 1, 'max_attempts': 3, 'resource': 'knowledge graph'}), {'decision': 'fail', 'reason': 'duplicate entity', 'resource': 'knowledge graph'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_graphrag_knowledge_system_duplicate_entity({'operation': 'link entity', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'knowledge graph'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'knowledge graph'})


if __name__ == "__main__":
    unittest.main()
