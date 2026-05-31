import unittest

from transport import Receiver, Segment


class ReliableReceiverTest(unittest.TestCase):
    def test_delivers_in_order(self):
        receiver = Receiver()
        self.assertEqual(receiver.receive(Segment(0, b"hel")), 3)
        self.assertEqual(receiver.receive(Segment(3, b"lo")), 5)
        self.assertEqual(receiver.read(), b"hello")

    def test_buffers_out_of_order(self):
        receiver = Receiver()
        self.assertEqual(receiver.receive(Segment(3, b"lo")), 0)
        self.assertEqual(receiver.read(), b"")
        self.assertEqual(receiver.receive(Segment(0, b"hel")), 5)
        self.assertEqual(receiver.read(), b"hello")

    def test_ignores_duplicate_segment(self):
        receiver = Receiver()
        self.assertEqual(receiver.receive(Segment(0, b"abc")), 3)
        self.assertEqual(receiver.receive(Segment(0, b"abc")), 3)
        self.assertEqual(receiver.read(), b"abc")


if __name__ == "__main__":
    unittest.main()

