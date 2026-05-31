import unittest

from lab import retrieve_context_document_chunk


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_document_chunk_request(self):
        self.assertEqual(retrieve_context_document_chunk({'id': 'document-chunk-001', 'kind': 'retrieve context', 'target': 'vector index', 'priority': 2, 'metadata': {'source': 'RAG From Scratch', 'track': 'ai-rag-agents'}}), {'id': 'document-chunk-001', 'action': 'retrieve context', 'target': 'vector index', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_document_chunk_request(self):
        self.assertEqual(retrieve_context_document_chunk({'id': 'bad', 'kind': '', 'target': 'vector index', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'vector index', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'document-chunk-001', 'kind': 'retrieve context', 'target': 'vector index', 'priority': 2, 'metadata': {'source': 'RAG From Scratch', 'track': 'ai-rag-agents'}}
        original = dict(request)
        retrieve_context_document_chunk(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
