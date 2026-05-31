import unittest
from lab import ApprovalWorkflow, InvalidTransition
class ApprovalTest(unittest.TestCase):
    def test_approval(self):
        w=ApprovalWorkflow(); i=w.request('delete'); self.assertFalse(w.can_execute(i)); w.approve(i); self.assertTrue(w.can_execute(i))
    def test_no_double_decision(self):
        w=ApprovalWorkflow(); i=w.request('delete'); w.reject(i)
        with self.assertRaises(InvalidTransition): w.approve(i)
if __name__ == '__main__': unittest.main()
