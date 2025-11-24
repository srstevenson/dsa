import unittest
from functools import cache


# time:  O(n)
# space: O(n)
@cache
def fib(n: int) -> int:
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(fib(0), 0)

    def test_01(self) -> None:
        self.assertEqual(fib(1), 1)

    def test_02(self) -> None:
        self.assertEqual(fib(2), 1)

    def test_03(self) -> None:
        self.assertEqual(fib(3), 2)

    def test_04(self) -> None:
        self.assertEqual(fib(4), 3)

    def test_05(self) -> None:
        self.assertEqual(fib(5), 5)

    def test_06(self) -> None:
        self.assertEqual(fib(35), 9_227_465)

    def test_07(self) -> None:
        self.assertEqual(fib(46), 1_836_311_903)


if __name__ == "__main__":
    unittest.main()
