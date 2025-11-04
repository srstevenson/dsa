import unittest


# time:  O(log n)
# space: O(1)
# where: n = len(numbers)
def binary_search(numbers: list[int], target: int) -> int:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid + 1
        elif numbers[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6), 6)

    def test_01(self) -> None:
        self.assertEqual(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27), -1)

    def test_02(self) -> None:
        self.assertEqual(binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8), 2)

    def test_03(self) -> None:
        self.assertEqual(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28), 8)

    def test_04(self) -> None:
        self.assertEqual(binary_search([7, 9], 7), 0)

    def test_05(self) -> None:
        self.assertEqual(binary_search([7, 9], 9), 1)

    def test_06(self) -> None:
        self.assertEqual(binary_search([7, 9], 12), -1)

    def test_07(self) -> None:
        self.assertEqual(binary_search([7], 7), 0)

    def test_08(self) -> None:
        self.assertEqual(binary_search([], 7), -1)


if __name__ == "__main__":
    unittest.main()
