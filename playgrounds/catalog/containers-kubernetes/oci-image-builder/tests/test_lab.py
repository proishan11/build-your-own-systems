import unittest
from lab import build_manifest
class ImageTest(unittest.TestCase):
    def test_manifest(self):
        m=build_manifest([b'a',b'bc']); self.assertEqual([l['size'] for l in m['layers']], [1,2]); self.assertTrue(m['layers'][0]['digest'].startswith('sha256:'))
    def test_deterministic(self): self.assertEqual(build_manifest([b'a']), build_manifest([b'a']))
if __name__ == '__main__': unittest.main()
