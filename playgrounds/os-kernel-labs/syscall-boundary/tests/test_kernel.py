import unittest

from kernel import BadAddress, BadFileDescriptor, Kernel, UserMemory


class SyscallBoundaryTest(unittest.TestCase):
    def test_sys_read_copies_to_user_memory(self):
        memory = UserMemory(16)
        kernel = Kernel(memory)
        kernel.open_bytes(3, b"hello")

        n = kernel.sys_read(3, 4, 3)

        self.assertEqual(n, 3)
        self.assertEqual(memory.read(4, 3), b"hel")

    def test_sys_read_advances_offset(self):
        memory = UserMemory(16)
        kernel = Kernel(memory)
        kernel.open_bytes(3, b"hello")

        self.assertEqual(kernel.sys_read(3, 0, 2), 2)
        self.assertEqual(kernel.sys_read(3, 2, 3), 3)
        self.assertEqual(memory.read(0, 5), b"hello")

    def test_rejects_bad_pointer(self):
        memory = UserMemory(4)
        kernel = Kernel(memory)
        kernel.open_bytes(3, b"hello")

        with self.assertRaises(BadAddress):
            kernel.sys_read(3, 3, 2)

    def test_rejects_bad_fd(self):
        memory = UserMemory(8)
        kernel = Kernel(memory)

        with self.assertRaises(BadFileDescriptor):
            kernel.sys_read(99, 0, 1)


if __name__ == "__main__":
    unittest.main()

