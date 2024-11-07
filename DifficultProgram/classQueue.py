class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
        >>> q = Queue(1, 2, 3, 4, 5, 6)
        >>> q.pop()
        1
        >>> q.pop()
        2
        >>> q.pop()
        3
        >>> q.pop()
        4
        >>> q.pop()
        5
        >>> q.pop()
        6
        >>> q.pop()
        'exception'
        >>> q.push(10)
        >>> q.push(11)
        >>> q.size
        2
        >>> q.is_empty()
        False
    """
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0
        for arg in args:
            self.push(arg)

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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
