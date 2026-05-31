import unittest
from lab import chunk, retrieve
class RAGTest(unittest.TestCase):
    def test_chunk_has_source(self): self.assertEqual(chunk('d1','a b c d',2,1)[0]['doc_id'],'d1')
    def test_retrieve(self):
        cs=[{'doc_id':'d1','text':'raft consensus log'}, {'doc_id':'d2','text':'banana'}]
        self.assertEqual(retrieve(cs,'raft log',1)[0]['doc_id'],'d1')
if __name__ == '__main__': unittest.main()
