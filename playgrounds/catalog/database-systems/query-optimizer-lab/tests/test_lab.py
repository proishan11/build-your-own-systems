import unittest
from lab import choose_plan
class PlannerTest(unittest.TestCase):
    def test_index_for_selective(self): self.assertEqual(choose_plan(1000, True, 0.01).kind, 'index_scan')
    def test_scan_without_index(self): self.assertEqual(choose_plan(1000, False, 0.01).kind, 'table_scan')
    def test_estimates_rows(self): self.assertEqual(choose_plan(1000, True, 0.25).estimated_rows, 250)
if __name__ == '__main__': unittest.main()
