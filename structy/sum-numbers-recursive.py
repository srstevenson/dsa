import unittest


# time:  O(n²)
# space: O(n²)
# where: n = len(numbers)
def sum_numbers_recursive(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(sum_numbers_recursive([5, 2, 9, 10]), 26)

    def test_01(self) -> None:
        self.assertEqual(sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]), 1)

    def test_02(self) -> None:
        self.assertEqual(sum_numbers_recursive([]), 0)

    def test_03(self) -> None:
        self.assertEqual(sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]), 1001)

    def test_04(self) -> None:
        self.assertEqual(sum_numbers_recursive([700, 70, 7]), 777)

    def test_05(self) -> None:
        self.assertEqual(
            sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), -55
        )

    def test_06(self) -> None:
        self.assertEqual(
            sum_numbers_recursive(
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            0,
        )

    def test_07(self) -> None:
        self.assertEqual(
            sum_numbers_recursive(
                [123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]
            ),
            137174205,
        )


if __name__ == "__main__":
    unittest.main()
