import unittest
from lab import recommend_indexes
class QueryPerfTest(unittest.TestCase):
    def test_recommend(self):
        qs=[{'calls':100,'total_ms':500,'filter':'user_id'}, {'calls':1,'total_ms':999,'filter':'debug'}]
        self.assertEqual(recommend_indexes(qs,10), ['user_id'])
if __name__ == '__main__': unittest.main()
