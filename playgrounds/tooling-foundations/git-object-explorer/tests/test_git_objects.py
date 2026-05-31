import unittest

from git_objects import GitObject, compress_loose_object, decode_loose_object, encode_blob, object_id


class GitObjectTest(unittest.TestCase):
    def test_encode_blob_and_hash(self):
        encoded = encode_blob(b"hello\n")
        self.assertEqual(encoded, b"blob 6\x00hello\n")
        self.assertEqual(object_id(encoded), "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_decode_loose_object(self):
        encoded = b"blob 6\x00hello\n"
        compressed = compress_loose_object(encoded)
        self.assertEqual(decode_loose_object(compressed), GitObject("blob", b"hello\n"))

    def test_decode_rejects_size_mismatch(self):
        compressed = compress_loose_object(b"blob 99\x00hello\n")
        with self.assertRaises(Exception):
            decode_loose_object(compressed)


if __name__ == "__main__":
    unittest.main()

