import unittest


# time:  O(n)
# space: O(1)
# where: n = len(s)
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(is_palindrome("pop"))

    def test_01(self) -> None:
        self.assertTrue(is_palindrome("kayak"))

    def test_02(self) -> None:
        self.assertFalse(is_palindrome("pops"))

    def test_03(self) -> None:
        self.assertFalse(is_palindrome("boot"))

    def test_04(self) -> None:
        self.assertTrue(is_palindrome("rotator"))

    def test_05(self) -> None:
        self.assertFalse(is_palindrome("abcbca"))

    def test_06(self) -> None:
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
