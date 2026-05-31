import unittest
from lab import NAT, NoMapping
class NATTest(unittest.TestCase):
    def test_outbound_reuses_mapping(self):
        n=NAT('203.0.113.1'); a=n.outbound('10.0.0.2',123,'8.8.8.8',53); b=n.outbound('10.0.0.2',123,'8.8.8.8',53); self.assertEqual(a,b)
    def test_inbound_reverse(self):
        n=NAT('203.0.113.1'); _,port=n.outbound('10.0.0.2',123,'8.8.8.8',53); self.assertEqual(n.inbound(port,'8.8.8.8',53), ('10.0.0.2',123))
    def test_unknown_inbound(self):
        with self.assertRaises(NoMapping): NAT('x').inbound(40000,'8.8.8.8',53)
if __name__ == '__main__': unittest.main()
