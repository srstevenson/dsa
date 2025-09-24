import unittest


# time:  O(n²)
# space: O(n²)
# where: n = len(s)
def reverse_string(s: str) -> str:
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_01(self) -> None:
        self.assertEqual(reverse_string("abcdefg"), "gfedcba")

    def test_02(self) -> None:
        self.assertEqual(reverse_string("stopwatch"), "hctawpots")

    def test_03(self) -> None:
        self.assertEqual(reverse_string(""), "")


if __name__ == "__main__":
    unittest.main()
