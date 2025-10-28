import unittest


# time:  O(n + c)
# space: O(n + c)
# where: n = len(s), c = len(chars)
def reverse_some_chars(s: str, chars: list[str]) -> str:
    chars_set = set(chars)
    stack = [c for c in s if c in chars_set]
    return "".join(stack.pop() if c in chars_set else c for c in s)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            reverse_some_chars("computer", ["a", "e", "i", "o", "u"]), "cemputor"
        )

    def test_01(self) -> None:
        self.assertEqual(
            reverse_some_chars("skateboard", ["a", "e", "i", "o", "u"]), "skatobeard"
        )

    def test_02(self) -> None:
        self.assertEqual(reverse_some_chars("airplane", ["m", "n", "r"]), "ainplare")

    def test_03(self) -> None:
        self.assertEqual(reverse_some_chars("building", ["g", "d", "i"]), "buglidni")


if __name__ == "__main__":
    unittest.main()
