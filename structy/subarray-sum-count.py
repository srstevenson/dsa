import unittest
from collections import defaultdict


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def subarray_sum_count(numbers: list[int], target_sum: int) -> int:
    prefix_sum = 0
    seen = defaultdict(int, {0: 1})
    count = 0
    for number in numbers:
        prefix_sum += number
        count += seen[prefix_sum - target_sum]
        seen[prefix_sum] += 1
    return count


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(subarray_sum_count([1, 3, 1, 4, -2, 3], 5), 3)

    def test_01(self) -> None:
        self.assertEqual(subarray_sum_count([1, 3, 1, 4, 3], 5), 2)

    def test_02(self) -> None:
        self.assertEqual(subarray_sum_count([1, 3, 1, 4, 3], 2), 0)

    def test_03(self) -> None:
        self.assertEqual(subarray_sum_count([1, 3, 1, 4, 3], 8), 2)

    def test_04(self) -> None:
        self.assertEqual(subarray_sum_count([1, 1, 1, 1], 2), 3)

    def test_05(self) -> None:
        self.assertEqual(subarray_sum_count([-2, 1, 1, 1, -1, 1, 1, 1, 1], 3), 8)


if __name__ == "__main__":
    unittest.main()
