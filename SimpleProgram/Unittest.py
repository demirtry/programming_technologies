import unittest
from Factorial import factorial_recursive


class TestWithUnittest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorial_recursive(-1), -1)

    def test_2(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_3(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_4(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_5(self):
        self.assertEqual(factorial_recursive(10), 3628800)


if __name__ == '__main__':
    unittest.main()
