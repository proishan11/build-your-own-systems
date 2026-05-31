import unittest
from lab import DuplicateResource, ResourceStore
class StoreTest(unittest.TestCase):
    def test_create_transition(self):
        s=ResourceStore(); s.create('x','new'); s.transition('x','ready'); self.assertEqual(s.get('x'),'ready')
    def test_duplicate(self):
        s=ResourceStore(); s.create('x','new')
        with self.assertRaises(DuplicateResource): s.create('x','new')
    def test_audit(self):
        s=ResourceStore(); s.create('x','new'); self.assertEqual(s.audit(), [('x','new')])
if __name__ == '__main__': unittest.main()
