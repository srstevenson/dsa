import unittest


# time:  O(n²)
# space: O(n)
# where: n = len(numbers)
def max_increasing_subseq(numbers: list[int]) -> int:
    dp = [1] * len(numbers)

    for i in range(len(numbers)):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        numbers = [4, 18, 20, 10, 12, 15, 19]
        self.assertEqual(max_increasing_subseq(numbers), 5)

    def test_01(self) -> None:
        numbers = [12, 9, 2, 5, 4, 32, 90, 20]
        self.assertEqual(max_increasing_subseq(numbers), 4)

    def test_02(self) -> None:
        numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
        self.assertEqual(max_increasing_subseq(numbers), 5)

    def test_03(self) -> None:
        numbers = [7, 14, 10, 12]
        self.assertEqual(max_increasing_subseq(numbers), 3)

    def test_04(self) -> None:
        numbers = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
        ]
        self.assertEqual(max_increasing_subseq(numbers), 21)

    def test_05(self) -> None:
        numbers = [
            1,
            2,
            3,
            4,
            5,
            12,
            6,
            30,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            10,
            18,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            100,
            104,
        ]
        self.assertEqual(max_increasing_subseq(numbers), 23)

    def test_06(self) -> None:
        numbers = [
            1,
            2,
            300,
            3,
            4,
            305,
            5,
            12,
            6,
            30,
            7,
            8,
            9,
            10,
            10,
            10,
            15,
            11,
            12,
            13,
            10,
            18,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            100,
            101,
            102,
            103,
            104,
            105,
        ]
        self.assertEqual(max_increasing_subseq(numbers), 27)

    def test_07(self) -> None:
        numbers = [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ]
        self.assertEqual(max_increasing_subseq(numbers), 1)

    def test_08(self) -> None:
        numbers = [
            1,
            2,
            300,
            3,
            4,
            305,
            5,
            10,
            7,
            10,
            6,
            12,
            6,
            30,
            7,
            8,
            9,
            10,
            10,
            16,
            14,
            9,
            10,
            15,
            11,
            12,
            13,
            10,
            18,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            100,
            101,
            102,
            103,
            104,
            105,
        ]
        self.assertEqual(max_increasing_subseq(numbers), 27)


if __name__ == "__main__":
    unittest.main()
