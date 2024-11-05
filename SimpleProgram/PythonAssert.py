from Factorial import factorial_recursive


def factorial_test():

    assert factorial_recursive(-1) == -1
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800

    print("All test cases passed!")


if __name__ == '__main__':
    factorial_test()
