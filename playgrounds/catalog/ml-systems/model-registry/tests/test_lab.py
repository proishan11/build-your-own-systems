import unittest
from lab import NotApproved, Registry
class RegistryTest(unittest.TestCase):
    def test_requires_approval(self):
        r=Registry(); v=r.register('m','uri',{})
        with self.assertRaises(NotApproved): r.promote(v)
    def test_promote_approved(self):
        r=Registry(); v=r.register('m','uri',{}); r.approve(v); r.promote(v); self.assertEqual(r.active(), v)
if __name__ == '__main__': unittest.main()
