import unittest


# time:  O(n)
# space: O(1)
# where: n = len(nums)
def non_adjacent_sum(nums: list[int]) -> int:
    if not nums:
        return 0

    prev2 = prev1 = 0

    for num in nums:
        max_sum = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = max_sum

    return prev1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        nums = [2, 4, 5, 12, 7]
        self.assertEqual(non_adjacent_sum(nums), 16)

    def test_01(self) -> None:
        nums = [7, 5, 5, 12]
        self.assertEqual(non_adjacent_sum(nums), 19)

    def test_02(self) -> None:
        nums = [7, 5, 5, 12, 17, 29]
        self.assertEqual(non_adjacent_sum(nums), 48)

    def test_03(self) -> None:
        nums = [
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            9,
            12,
            3,
            1,
            19,
            30,
            50,
            20,
        ]
        self.assertEqual(non_adjacent_sum(nums), 488)

    def test_04(self) -> None:
        nums = [
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            83,
            80,
            56,
            68,
            6,
            22,
            56,
            96,
            77,
            98,
            61,
            20,
            0,
            76,
            53,
            74,
            8,
            22,
            92,
            37,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            42,
        ]
        self.assertEqual(non_adjacent_sum(nums), 1465)


if __name__ == "__main__":
    unittest.main()
