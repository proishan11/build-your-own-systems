import unittest
from lab import DNSError, decode_name, encode_name
class DNSTest(unittest.TestCase):
    def test_round_trip(self):
        data=encode_name('www.example.com'); self.assertEqual(data, b'\x03www\x07example\x03com\x00'); self.assertEqual(decode_name(data), ('www.example.com', len(data)))
    def test_reject_long_label(self):
        with self.assertRaises(DNSError): encode_name('a'*64+'.com')
if __name__ == '__main__': unittest.main()
