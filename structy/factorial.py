import unittest
from functools import cache


# time:  O(n)
# space: O(n)
@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(factorial(3), 6)

    def test_01(self) -> None:
        self.assertEqual(factorial(6), 720)

    def test_02(self) -> None:
        self.assertEqual(factorial(18), 6402373705728000)

    def test_03(self) -> None:
        self.assertEqual(factorial(1), 1)

    def test_04(self) -> None:
        self.assertEqual(factorial(13), 6227020800)

    def test_05(self) -> None:
        self.assertEqual(factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
