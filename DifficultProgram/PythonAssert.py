from classQueue import Queue


def test_queue_working():
    queue = Queue(1, 2, 3, 4, 5, 6)
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() == 6
    assert queue.pop() == 'exception'
    queue.push(10)
    queue.push(11)
    assert queue.size == 2
    assert queue.is_empty() is False

    print("All test cases passed!")


if __name__ == '__main__':
    test_queue_working()
