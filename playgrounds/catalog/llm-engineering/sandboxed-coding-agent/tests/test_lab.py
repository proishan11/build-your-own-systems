import unittest
from lab import classify
class SandboxTest(unittest.TestCase):
    def test_allow_read(self): self.assertEqual(classify(['ls'])[0], 'allow')
    def test_deny_rm(self): self.assertEqual(classify(['rm','-rf','/tmp/x'])[0], 'deny')
    def test_approval_network(self): self.assertEqual(classify(['curl','https://example.com'])[0], 'approval')
if __name__ == '__main__': unittest.main()
