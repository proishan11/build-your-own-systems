import unittest
from lab import SessionStore
class SessionTest(unittest.TestCase):
    def test_create_get(self):
        s=SessionStore(); sid=s.create('u'); self.assertEqual(s.get(sid),'u')
    def test_rotate_invalidates_old(self):
        s=SessionStore(); old=s.create('u'); new=s.rotate(old); self.assertIsNone(s.get(old)); self.assertEqual(s.get(new),'u')
if __name__ == '__main__': unittest.main()
