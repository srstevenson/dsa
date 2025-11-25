import unittest
from functools import cache


# time:  O(n)
# space: O(n)
@cache
def tribonacci(n: int) -> int:
    if n in (0, 1):
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(tribonacci(0), 0)

    def test_01(self) -> None:
        self.assertEqual(tribonacci(1), 0)

    def test_02(self) -> None:
        self.assertEqual(tribonacci(2), 1)

    def test_03(self) -> None:
        self.assertEqual(tribonacci(5), 4)

    def test_04(self) -> None:
        self.assertEqual(tribonacci(7), 13)

    def test_05(self) -> None:
        self.assertEqual(tribonacci(14), 927)

    def test_06(self) -> None:
        self.assertEqual(tribonacci(20), 35890)

    def test_07(self) -> None:
        self.assertEqual(tribonacci(37), 1132436852)


if __name__ == "__main__":
    unittest.main()
