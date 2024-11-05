class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        self.size += 1
        current_node = Node(value)
        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

    def pop(self):
        if not self.is_empty():
            current_node = self.head
            self.head = current_node.next
            self.size -= 1

            return current_node.value
        return "exception"

    def is_empty(self):
        return not self.size


def test_queue_working():
    # проверка работоспособности очереди в т.ч получение элементов в нужном порядке,
    # обработка исключений, контроль размера очереди
    queue1 = Queue()
    queue1.push(10)
    queue1.push(11)
    assert queue1.pop() == 10
    assert queue1.size == 1
    assert queue1.pop() == 11
    assert queue1.size == 0
    assert queue1.pop() == 'exception'
    print('all good')


if __name__ == '__main__':
    test_queue_working()
