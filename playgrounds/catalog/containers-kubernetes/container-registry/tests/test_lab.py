import unittest
from lab import BlobInUse, Registry
class RegistryTest(unittest.TestCase):
    def test_blob_digest(self):
        r=Registry(); d=r.put_blob(b'a'); self.assertTrue(d.startswith('sha256:')); self.assertTrue(r.has_blob(d))
    def test_prevent_delete_referenced(self):
        r=Registry(); d=r.put_blob(b'a'); r.put_manifest('img',[d])
        with self.assertRaises(BlobInUse): r.delete_blob(d)
if __name__ == '__main__': unittest.main()
