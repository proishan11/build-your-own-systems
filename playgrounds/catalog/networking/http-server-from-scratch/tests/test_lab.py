import unittest
from lab import BadRequest, parse_request
class HTTPTest(unittest.TestCase):
    def test_parse_request(self):
        r=parse_request('GET /x HTTP/1.1\r\nHost: example.com\r\nX-Test: ok\r\n\r\n')
        self.assertEqual((r.method,r.path,r.version), ('GET','/x','HTTP/1.1')); self.assertEqual(r.headers['host'],'example.com')
    def test_reject_bad_line(self):
        with self.assertRaises(BadRequest): parse_request('GET-only\r\n\r\n')
if __name__ == '__main__': unittest.main()
