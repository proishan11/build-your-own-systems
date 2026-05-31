import unittest
from lab import Allocator, InvalidFree, OutOfMemory
class AllocatorTest(unittest.TestCase):
    def test_allocates_distinct_blocks(self):
        a=Allocator(16); self.assertEqual(a.alloc(4),0); self.assertEqual(a.alloc(4),4)
    def test_reuses_freed_block(self):
        a=Allocator(16); x=a.alloc(4); a.free(x); self.assertEqual(a.alloc(3),0)
    def test_reports_out_of_memory(self):
        a=Allocator(8); a.alloc(8)
        with self.assertRaises(OutOfMemory): a.alloc(1)
    def test_rejects_double_free(self):
        a=Allocator(8); x=a.alloc(2); a.free(x)
        with self.assertRaises(InvalidFree): a.free(x)
if __name__ == '__main__': unittest.main()
