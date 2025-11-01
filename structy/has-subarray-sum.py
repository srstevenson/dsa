import unittest


# time:  O(n²)
# space: O(1)
# where: n = len(numbers)
def has_subarray_sum(numbers: list[int], target_sum: int) -> bool:
    for left_idx in range(len(numbers)):
        total = 0
        for right_idx in range(left_idx, len(numbers)):
            if (total := total + numbers[right_idx]) == target_sum:
                return True
    return False


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def has_subarray_sum_with_space(numbers: list[int], target_sum: int) -> bool:
    prefix_sum = 0
    seen = {prefix_sum}
    for number in numbers:
        prefix_sum += number
        if prefix_sum - target_sum in seen:
            return True
        seen.add(prefix_sum)
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertTrue(solution([1, 3, 1, 4, 3], 8))

    def test_01(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertFalse(solution([1, 3, 1, 4, 3], 2))

    def test_02(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertTrue(solution([1, 3, 1, 1, 3], 2))

    def test_03(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertTrue(solution([5], 5))

    def test_04(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertTrue(solution([4, 2, 5, 1, 5, -2, 8], 9))

    def test_05(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertFalse(solution([4, 2, 5, 1, 5, -2, 8], 10))

    def test_06(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertTrue(solution([1, 1, 1, 1, 1, 1, 1, 1, 1], 9))

    def test_07(self) -> None:
        for solution in [has_subarray_sum, has_subarray_sum_with_space]:
            self.assertFalse(solution([1, 1, 1, 1, 1, 1, 1, 1, 1], 10))


if __name__ == "__main__":
    unittest.main()
