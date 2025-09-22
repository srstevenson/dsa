import unittest


# time:  O(n)
# space: O(1)
# where: n = len(nums)
def five_sort(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != 5:
            left += 1
        elif nums[right] == 5:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    return nums


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        nums = [5, 0]
        five_sort(nums)
        self.assertEqual(nums, [0, 5])

    def test_01(self) -> None:
        nums = [12, 5, 1, 5, 12, 7]
        five_sort(nums)
        self.assertEqual(nums, [12, 7, 1, 12, 5, 5])

    def test_02(self) -> None:
        nums = [5, 2, 5, 6, 5, 1, 10, 2, 5, 5]
        five_sort(nums)
        self.assertEqual(nums, [2, 2, 10, 6, 1, 5, 5, 5, 5, 5])

    def test_03(self) -> None:
        nums = [5, 5, 5, 1, 1, 1, 4]
        five_sort(nums)
        self.assertEqual(nums, [4, 1, 1, 1, 5, 5, 5])

    def test_04(self) -> None:
        nums = [5, 5, 6, 5, 5, 5, 5]
        five_sort(nums)
        self.assertEqual(nums, [6, 5, 5, 5, 5, 5, 5])

    def test_05(self) -> None:
        nums = [5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]
        five_sort(nums)
        self.assertEqual(nums, [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5])

    def test_06(self) -> None:
        fours = [4] * 20_000
        fives = [5] * 20_000
        nums = fours + fives
        five_sort(nums)
        self.assertTrue(all(num == 4 for num in nums[:20_000]))
        self.assertTrue(all(num == 5 for num in nums[20_000:]))


if __name__ == "__main__":
    unittest.main()
