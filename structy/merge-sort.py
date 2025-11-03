import unittest


# time:  O(n log n)
# space: O(n)
# where: n = len(nums)
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[mid:])
    right = merge_sort(nums[:mid])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
        self.assertEqual(merge_sort(numbers), [4, 5, 5, 6, 8, 10, 12, 40, 42, 100])

    def test_01(self) -> None:
        numbers = [7, -30, -4, -1, 12, 0, 20]
        self.assertEqual(merge_sort(numbers), [-30, -4, -1, 0, 7, 12, 20])

    def test_02(self) -> None:
        numbers = [8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(merge_sort(numbers), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_03(self) -> None:
        numbers = [
            72,
            42,
            16,
            81,
            84,
            17,
            2,
            81,
            22,
            79,
            86,
            38,
            77,
            80,
            81,
            70,
            81,
            80,
            35,
            21,
            89,
            38,
            57,
            28,
            4,
            17,
            50,
            38,
            68,
            82,
            22,
            76,
            45,
            40,
            67,
            94,
            37,
            27,
            81,
            53,
            36,
            18,
            28,
            60,
            45,
            74,
            40,
            29,
            18,
            6,
            28,
            57,
            42,
            60,
            64,
            12,
            78,
            97,
            96,
            1,
            20,
            20,
            61,
            67,
            82,
            10,
            63,
            71,
            39,
            52,
            37,
            69,
            37,
            24,
            66,
            74,
            15,
            92,
            49,
            31,
            56,
            67,
            50,
            57,
            79,
            0,
            21,
            56,
            82,
            22,
            4,
            20,
            91,
            72,
            58,
            93,
            99,
            14,
            42,
            91,
        ]
        self.assertEqual(
            merge_sort(numbers),
            [
                0,
                1,
                2,
                4,
                4,
                6,
                10,
                12,
                14,
                15,
                16,
                17,
                17,
                18,
                18,
                20,
                20,
                20,
                21,
                21,
                22,
                22,
                22,
                24,
                27,
                28,
                28,
                28,
                29,
                31,
                35,
                36,
                37,
                37,
                37,
                38,
                38,
                38,
                39,
                40,
                40,
                42,
                42,
                42,
                45,
                45,
                49,
                50,
                50,
                52,
                53,
                56,
                56,
                57,
                57,
                57,
                58,
                60,
                60,
                61,
                63,
                64,
                66,
                67,
                67,
                67,
                68,
                69,
                70,
                71,
                72,
                72,
                74,
                74,
                76,
                77,
                78,
                79,
                79,
                80,
                80,
                81,
                81,
                81,
                81,
                81,
                82,
                82,
                82,
                84,
                86,
                89,
                91,
                91,
                92,
                93,
                94,
                96,
                97,
                99,
            ],
        )

    def test_04(self) -> None:
        numbers = [7] * 95_000
        self.assertEqual(merge_sort(numbers), [7] * 95_000)

    def test_05(self) -> None:
        numbers = [7] * 120_000
        self.assertEqual(merge_sort(numbers), [7] * 120_000)


if __name__ == "__main__":
    unittest.main()
