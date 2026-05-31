import unittest

from vm import AddressSpace, PageFault


class VirtualMemoryTest(unittest.TestCase):
    def test_translates_mapped_address(self):
        space = AddressSpace(page_size=4096)
        space.map_page(2, frame=7, readable=True, writable=True)
        self.assertEqual(space.translate(2 * 4096 + 123), 7 * 4096 + 123)

    def test_rejects_unmapped_page(self):
        space = AddressSpace(page_size=4096)
        with self.assertRaises(PageFault):
            space.translate(0)

    def test_enforces_write_permission(self):
        space = AddressSpace(page_size=4096)
        space.map_page(1, frame=4, readable=True, writable=False)
        self.assertEqual(space.translate(4096), 4 * 4096)
        with self.assertRaises(PageFault):
            space.translate(4096, write=True)


if __name__ == "__main__":
    unittest.main()

