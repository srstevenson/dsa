import unittest
from math import isqrt


# time:  O(√n)
# space: O(1)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, isqrt(n) + 1, 2))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(is_prime(2))

    def test_01(self) -> None:
        self.assertTrue(is_prime(3))

    def test_02(self) -> None:
        self.assertFalse(is_prime(4))

    def test_03(self) -> None:
        self.assertTrue(is_prime(5))

    def test_04(self) -> None:
        self.assertFalse(is_prime(6))

    def test_05(self) -> None:
        self.assertTrue(is_prime(7))

    def test_06(self) -> None:
        self.assertFalse(is_prime(8))

    def test_07(self) -> None:
        self.assertFalse(is_prime(25))

    def test_08(self) -> None:
        self.assertTrue(is_prime(31))

    def test_09(self) -> None:
        self.assertTrue(is_prime(2017))

    def test_10(self) -> None:
        self.assertFalse(is_prime(2048))

    def test_11(self) -> None:
        self.assertFalse(is_prime(1))

    def test_12(self) -> None:
        self.assertFalse(is_prime(713))


if __name__ == "__main__":
    unittest.main()
