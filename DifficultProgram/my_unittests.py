import unittest
from classQueue import Queue


# расширяю функционал очереди для проверки значений
class AdaptedToTestsQueue(Queue):
    def __init__(self):
        super().__init__()

    def peek_first(self):
        if self.head is None:
            return None
        print(self.head.value)
        return self.head.value


class TestWithUnittest(unittest.TestCase):
    def setUp(self):
        self.queue = AdaptedToTestsQueue()

    def test_add1(self):
        # проверка добавляения в очередь
        self.queue.push(100)
        self.queue.push(200)
        self.assertEqual(self.queue.peek_first(), 100)

    def test_size(self):
        # проверка добавляения в очередь
        self.queue.push(100)
        self.queue.push(200)
        self.assertEqual(self.queue.size, 2)

    def test_pop(self):
        self.queue.push(100)
        self.queue.push(200)
        self.assertEqual(self.queue.pop(), 200)

    def test_size_after_pop(self):
        self.queue.push(100)
        self.queue.push(200)
        self.queue.pop()
        self.assertEqual(self.queue.size, 1)


if __name__ == '__main__':
    unittest.main()
