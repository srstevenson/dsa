import unittest


# time:  O(n²)
# space: O(n²)
# where: n = len(strings)
def sum_of_lengths(strings: list[str]) -> int:
    if not strings:
        return 0
    return len(strings[0]) + sum_of_lengths(strings[1:])


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(sum_of_lengths(["goat", "cat", "purple"]), 13)

    def test_01(self) -> None:
        self.assertEqual(sum_of_lengths(["bike", "at", "pencils", "phone"]), 18)

    def test_02(self) -> None:
        self.assertEqual(sum_of_lengths([]), 0)

    def test_03(self) -> None:
        self.assertEqual(sum_of_lengths(["", " ", "  ", "   ", "    ", "     "]), 15)

    def test_04(self) -> None:
        self.assertEqual(sum_of_lengths(["0", "313", "1234567890"]), 14)


if __name__ == "__main__":
    unittest.main()
