import unittest
from lab import enabled
class FlagTest(unittest.TestCase):
    def test_off(self): self.assertFalse(enabled({'on':False}, 'u1'))
    def test_target(self): self.assertTrue(enabled({'on':True,'targets':['u1'],'percent':0}, 'u1'))
    def test_deterministic(self):
        f={'on':True,'targets':[],'percent':50}; self.assertEqual(enabled(f,'u2'), enabled(f,'u2'))
if __name__ == '__main__': unittest.main()
