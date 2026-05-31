import unittest

from lab import link_entity_entity_mention


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_entity_mention_request(self):
        self.assertEqual(link_entity_entity_mention({'id': 'entity-mention-001', 'kind': 'link entity', 'target': 'knowledge graph', 'priority': 2, 'metadata': {'source': 'GraphRAG Knowledge System', 'track': 'ai-rag-agents'}}), {'id': 'entity-mention-001', 'action': 'link entity', 'target': 'knowledge graph', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_entity_mention_request(self):
        self.assertEqual(link_entity_entity_mention({'id': 'bad', 'kind': '', 'target': 'knowledge graph', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'knowledge graph', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'entity-mention-001', 'kind': 'link entity', 'target': 'knowledge graph', 'priority': 2, 'metadata': {'source': 'GraphRAG Knowledge System', 'track': 'ai-rag-agents'}}
        original = dict(request)
        link_entity_entity_mention(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
