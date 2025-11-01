import unittest


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def running_sum(numbers: list[int]) -> list[int]:
    total = 0
    result: list[int] = []
    for number in numbers:
        total += number
        result.append(total)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(running_sum([4, 2, 1, 6, 3, 6]), [4, 6, 7, 13, 16, 22])

    def test_01(self) -> None:
        self.assertEqual(running_sum([10, 5, -2, 1, 1]), [10, 15, 13, 14, 15])

    def test_02(self) -> None:
        self.assertEqual(
            running_sum([12, 88, 0, -50, 30, 2]), [12, 100, 100, 50, 80, 82]
        )

    def test_03(self) -> None:
        self.assertEqual(running_sum([2]), [2])

    def test_04(self) -> None:
        self.assertEqual(running_sum([]), [])


if __name__ == "__main__":
    unittest.main()
