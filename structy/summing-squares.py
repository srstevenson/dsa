import math
import sys
import unittest


# time:  O(n√n)
# space: O(n)
def summing_squares(n: int) -> int:
    squares = [i**2 for i in range(1, math.isqrt(n) + 1)]

    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for square in squares:
        for i in range(square, n + 1):
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[n]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(summing_squares(8), 2)

    def test_01(self) -> None:
        self.assertEqual(summing_squares(9), 1)

    def test_02(self) -> None:
        self.assertEqual(summing_squares(12), 3)

    def test_03(self) -> None:
        self.assertEqual(summing_squares(1), 1)

    def test_04(self) -> None:
        self.assertEqual(summing_squares(31), 4)

    def test_05(self) -> None:
        self.assertEqual(summing_squares(50), 2)

    def test_06(self) -> None:
        self.assertEqual(summing_squares(68), 2)

    def test_07(self) -> None:
        self.assertEqual(summing_squares(87), 4)


if __name__ == "__main__":
    unittest.main()
