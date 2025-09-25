import unittest


# time:  O(n²)
# space: O(n²)
# where: n = len(s)
def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(palindrome("pop"))

    def test_01(self) -> None:
        self.assertTrue(palindrome("kayak"))

    def test_02(self) -> None:
        self.assertFalse(palindrome("pops"))

    def test_03(self) -> None:
        self.assertFalse(palindrome("boot"))

    def test_04(self) -> None:
        self.assertTrue(palindrome("rotator"))

    def test_05(self) -> None:
        self.assertFalse(palindrome("abcbca"))

    def test_06(self) -> None:
        self.assertTrue(palindrome(""))


if __name__ == "__main__":
    unittest.main()
