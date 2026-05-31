import unittest
from lab import can_read, denied_event
class AuthzTest(unittest.TestCase):
    def test_owner(self): self.assertTrue(can_read({'id':'u1','role':'user'}, {'owner':'u1'}))
    def test_admin(self): self.assertTrue(can_read({'id':'a','role':'admin'}, {'owner':'u1'}))
    def test_denied(self): self.assertFalse(can_read({'id':'u2','role':'user'}, {'owner':'u1'})); self.assertEqual(denied_event({'id':'u2'}, {'owner':'u1'})['actor'], 'u2')
if __name__ == '__main__': unittest.main()
