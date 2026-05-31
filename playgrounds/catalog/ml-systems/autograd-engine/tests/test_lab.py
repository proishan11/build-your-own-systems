import unittest
from lab import Value
class AutogradTest(unittest.TestCase):
    def test_mul_grad(self):
        x=Value(3); y=Value(4); z=x*y; z.backward(); self.assertEqual((x.grad,y.grad),(4,3))
    def test_add_grad(self):
        x=Value(3); y=Value(4); z=x+y; z.backward(); self.assertEqual((x.grad,y.grad),(1,1))
if __name__ == '__main__': unittest.main()
