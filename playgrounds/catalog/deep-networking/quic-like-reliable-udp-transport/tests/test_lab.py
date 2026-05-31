import unittest
from lab import StreamReassembler
class ReassemblerTest(unittest.TestCase):
    def test_in_order(self):
        r=StreamReassembler(); self.assertEqual(r.push(0,b'he'), b'he'); self.assertEqual(r.push(2,b'y'), b'y')
    def test_out_of_order(self):
        r=StreamReassembler(); self.assertEqual(r.push(2,b'y'), b''); self.assertEqual(r.push(0,b'he'), b'hey')
    def test_duplicate(self):
        r=StreamReassembler(); r.push(0,b'abc'); self.assertEqual(r.push(0,b'abc'), b''); self.assertEqual(r.next_offset(),3)
if __name__ == '__main__': unittest.main()
