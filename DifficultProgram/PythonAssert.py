from classQueue import Queue


def test_queue_working():
    queue1 = Queue()
    queue1.push(10)
    queue1.push(11)
    assert queue1.pop() == 10
    assert queue1.size == 1
    assert queue1.pop() == 11
    assert queue1.size == 0
    assert queue1.pop() == 'exception'

    print("All test cases passed!")


if __name__ == '__main__':
    test_queue_working()
    