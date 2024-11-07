class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
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
