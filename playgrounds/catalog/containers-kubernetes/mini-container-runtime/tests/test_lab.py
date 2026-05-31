import unittest
from lab import SpecError, validate_spec
class ContainerTest(unittest.TestCase):
    def test_defaults_drop_caps(self): self.assertFalse(validate_spec({'rootfs':'/x','argv':['sh']})['privileged'])
    def test_reject_privileged(self):
        with self.assertRaises(SpecError): validate_spec({'rootfs':'/x','argv':['sh'], 'privileged':True})
if __name__ == '__main__': unittest.main()
