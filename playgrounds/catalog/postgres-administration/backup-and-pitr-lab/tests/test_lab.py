import unittest
from lab import RestoreError, plan_restore
class RestoreTest(unittest.TestCase):
    def test_plan(self): self.assertEqual(plan_restore([10,20], [(20,30),(30,40)], 35)['backup'],20)
    def test_reject_too_early(self):
        with self.assertRaises(RestoreError): plan_restore([10], [], 5)
if __name__ == '__main__': unittest.main()
