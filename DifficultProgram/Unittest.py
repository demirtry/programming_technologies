from classQueue import Queue
import unittest


queue = Queue(1, 2, 3, 4, 5, 6)


class TestQueue(unittest.TestCase):
    def test_pop(self):
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 4)
        self.assertEqual(queue.pop(), 5)
        self.assertEqual(queue.pop(), 6)
        self.assertEqual(queue.pop(), "exception")

    def test_push(self):
        queue.push(10)
        queue.push(11)
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.is_empty(), False)


if __name__ == "__main__":
    unittest.main()
