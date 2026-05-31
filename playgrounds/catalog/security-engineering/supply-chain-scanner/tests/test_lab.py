import unittest
from lab import scan
class SupplyTest(unittest.TestCase):
    def test_findings(self):
        deps={'lib':'2'}; adv=[{'package':'lib','lt':'3','id':'CVE-1'}]; self.assertEqual(scan(deps,adv)[0]['id'], 'CVE-1')
    def test_unaffected(self): self.assertEqual(scan({'lib':'4'}, [{'package':'lib','lt':'3','id':'CVE'}]), [])
if __name__ == '__main__': unittest.main()
