import unittest


# time:  O(n)
# space: O(n)
# where: n = len(string)
def befitting_brackets(string: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}

    stack: list[str] = []
    for char in string:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(befitting_brackets("(){}[](())"))

    def test_01(self) -> None:
        self.assertTrue(befitting_brackets("({[]})"))

    def test_02(self) -> None:
        self.assertFalse(befitting_brackets("[][}"))

    def test_03(self) -> None:
        self.assertFalse(befitting_brackets("{[]}({}"))

    def test_04(self) -> None:
        self.assertFalse(befitting_brackets("[]{}(}[]"))

    def test_05(self) -> None:
        self.assertTrue(befitting_brackets("[]{}()[]"))

    def test_06(self) -> None:
        self.assertFalse(befitting_brackets("]{}"))

    def test_07(self) -> None:
        self.assertTrue(befitting_brackets(""))

    def test_08(self) -> None:
        self.assertFalse(befitting_brackets("{[(}])"))


if __name__ == "__main__":
    unittest.main()
