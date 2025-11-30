import unittest


# time:  O(n²)
# space: O(n)
# where: n = len(numbers)
def array_stepper(numbers: list[int]) -> bool:
    dp = [False for _ in numbers]
    dp[0] = True

    for idx, val in enumerate(numbers):
        for steps in range(1, val + 1):
            if idx + steps == len(numbers) - 1:
                return True
            if idx + steps < len(numbers):
                dp[idx + steps] = True

    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(array_stepper([2, 4, 2, 0, 0, 1]))

    def test_01(self) -> None:
        self.assertFalse(array_stepper([2, 3, 2, 0, 0, 1]))

    def test_02(self) -> None:
        self.assertTrue(array_stepper([3, 1, 3, 1, 0, 1]))

    def test_03(self) -> None:
        self.assertTrue(array_stepper([4, 1, 5, 1, 1, 1, 0, 4]))

    def test_04(self) -> None:
        self.assertFalse(array_stepper([4, 1, 2, 1, 1, 1, 0, 4]))

    def test_05(self) -> None:
        self.assertTrue(array_stepper([1, 1, 1, 1, 1, 0]))

    def test_06(self) -> None:
        self.assertFalse(array_stepper([1, 1, 1, 1, 0, 0]))

    def test_07(self) -> None:
        self.assertFalse(
            array_stepper(
                [
                    31,
                    30,
                    29,
                    28,
                    27,
                    26,
                    25,
                    24,
                    23,
                    22,
                    21,
                    20,
                    19,
                    18,
                    17,
                    16,
                    15,
                    14,
                    13,
                    12,
                    11,
                    10,
                    9,
                    8,
                    7,
                    6,
                    5,
                    3,
                    2,
                    1,
                    0,
                    0,
                    0,
                ]
            )
        )


if __name__ == "__main__":
    unittest.main()
