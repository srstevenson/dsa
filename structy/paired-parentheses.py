import unittest


# time:  O(n)
# space: O(1)
# where: n = len(string)
def paired_parentheses(string: str) -> bool:
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(paired_parentheses("(david)((abby))"))

    def test_01(self) -> None:
        self.assertFalse(paired_parentheses("()rose(jeff"))

    def test_02(self) -> None:
        self.assertFalse(paired_parentheses(")("))

    def test_03(self) -> None:
        self.assertTrue(paired_parentheses("()"))

    def test_04(self) -> None:
        self.assertTrue(paired_parentheses("(((potato())))"))

    def test_05(self) -> None:
        self.assertTrue(paired_parentheses("(())(water)()"))

    def test_06(self) -> None:
        self.assertFalse(paired_parentheses("(())(water()()"))

    def test_07(self) -> None:
        self.assertTrue(paired_parentheses(""))

    def test_08(self) -> None:
        self.assertFalse(paired_parentheses("))()"))


if __name__ == "__main__":
    unittest.main()
