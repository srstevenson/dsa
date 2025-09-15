import unittest


# time:  O(n)
# space: O(1)
# where: n = len(nums)
def max_value(nums: list[float]) -> float:
    max_seen = nums[0]
    for num in nums:
        max_seen = max(num, max_seen)
    return max_seen


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(max_value([4, 7, 2, 8, 10, 9]), 10)

    def test_01(self) -> None:
        self.assertEqual(max_value([10, 5, 40, 40.3]), 40.3)

    def test_02(self) -> None:
        self.assertEqual(max_value([-5, -2, -1, -11]), -1)

    def test_03(self) -> None:
        self.assertEqual(max_value([42]), 42)

    def test_04(self) -> None:
        self.assertEqual(max_value([1000, 8]), 1000)

    def test_05(self) -> None:
        self.assertEqual(max_value([1000, 8, 9000]), 9000)

    def test_06(self) -> None:
        self.assertEqual(max_value([2, 5, 1, 1, 4]), 5)


if __name__ == "__main__":
    unittest.main()
