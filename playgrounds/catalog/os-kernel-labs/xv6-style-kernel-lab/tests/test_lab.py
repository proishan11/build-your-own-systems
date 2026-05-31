import unittest
from lab import AddressSpace, PageFault
class VMTest(unittest.TestCase):
    def test_translate(self):
        a=AddressSpace(); a.map(2,7,write=True); self.assertEqual(a.translate(2*4096+9), 7*4096+9)
    def test_unmapped_fault(self):
        with self.assertRaises(PageFault): AddressSpace().translate(0)
    def test_write_permission(self):
        a=AddressSpace(); a.map(1,4,write=False)
        with self.assertRaises(PageFault): a.translate(4096, write=True)
if __name__ == '__main__': unittest.main()
