import unittest
from lab import ValidationError, validate
class ValidatorTest(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate({'a':1},{'a':int}), {'a':1})
    def test_reports_errors(self):
        with self.assertRaises(ValidationError) as cm: validate({'a':'x'}, {'a':int,'b':str})
        self.assertGreaterEqual(len(cm.exception.errors), 2)
if __name__ == '__main__': unittest.main()
