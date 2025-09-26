import unittest
from functools import cache


# time:  O(n)
# space: O(n)
@cache
def fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(fibonacci(0), 0)

    def test_01(self) -> None:
        self.assertEqual(fibonacci(1), 1)

    def test_02(self) -> None:
        self.assertEqual(fibonacci(2), 1)

    def test_03(self) -> None:
        self.assertEqual(fibonacci(3), 2)

    def test_04(self) -> None:
        self.assertEqual(fibonacci(4), 3)

    def test_05(self) -> None:
        self.assertEqual(fibonacci(5), 5)

    def test_06(self) -> None:
        self.assertEqual(fibonacci(8), 21)


if __name__ == "__main__":
    unittest.main()
