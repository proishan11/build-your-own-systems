import unittest
from lab import reconcile
class ReconcileTest(unittest.TestCase):
    def test_create(self): self.assertEqual(reconcile(3,['a'])['action'], 'create')
    def test_delete(self): self.assertEqual(reconcile(1,['a','b'])['action'], 'delete')
    def test_noop(self): self.assertEqual(reconcile(2,['a','b'])['action'], 'noop')
if __name__ == '__main__': unittest.main()
