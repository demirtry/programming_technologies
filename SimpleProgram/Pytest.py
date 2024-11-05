from Factorial import factorial_recursive
import pytest


def test_1():
    assert factorial_recursive(-1) == -1


def test_2():
    assert factorial_recursive(0) == 1


def test_3():
    assert factorial_recursive(1) == 1


def test_4():
    assert factorial_recursive(5) == 120


def test_5():
    assert factorial_recursive(10) == 3628800


if __name__ == '__main__':
    pytest.main()
