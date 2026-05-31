import unittest
from lab import AccessDenied, SecretStore
class SecretTest(unittest.TestCase):
    def test_access(self):
        s=SecretStore(); s.put('db','pw', {'alice'}); self.assertEqual(s.get('alice','db'),'pw')
    def test_denied(self):
        s=SecretStore(); s.put('db','pw', {'alice'})
        with self.assertRaises(AccessDenied): s.get('bob','db')
    def test_audit_redacts(self):
        s=SecretStore(); s.put('db','pw', {'alice'}); s.get('alice','db'); self.assertNotIn('pw', str(s.audit()))
if __name__ == '__main__': unittest.main()
