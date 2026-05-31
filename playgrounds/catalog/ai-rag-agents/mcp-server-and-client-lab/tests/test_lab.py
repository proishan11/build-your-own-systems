import unittest
from lab import ToolError, ToolRegistry
class ToolTest(unittest.TestCase):
    def test_call(self):
        r=ToolRegistry(); r.register('read', {'path'}); self.assertEqual(r.call('read', {'path':'x'})['tool'],'read')
    def test_missing_arg(self):
        r=ToolRegistry(); r.register('read', {'path'})
        with self.assertRaises(ToolError): r.call('read', {})
    def test_audit(self):
        r=ToolRegistry(); r.register('read', set()); r.call('read', {}); self.assertEqual(len(r.calls()),1)
if __name__ == '__main__': unittest.main()
