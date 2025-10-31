import unittest


# time:  O(n)
# space: O(n)
# where: n = len(string)
def nesting_score(string: str) -> int:
    stack = [0]
    for char in string:
        if char == "[":
            stack.append(0)
        else:
            top = stack.pop()
            stack[-1] += 1 if top == 0 else 2 * top
    return stack[0]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(nesting_score("[]"), 1)

    def test_01(self) -> None:
        self.assertEqual(nesting_score("[][][]"), 3)

    def test_02(self) -> None:
        self.assertEqual(nesting_score("[[]]"), 2)

    def test_03(self) -> None:
        self.assertEqual(nesting_score("[[][]]"), 4)

    def test_04(self) -> None:
        self.assertEqual(nesting_score("[[][][]]"), 6)

    def test_05(self) -> None:
        self.assertEqual(nesting_score("[[][]][]"), 5)

    def test_06(self) -> None:
        self.assertEqual(nesting_score("[][[][]][[]]"), 7)

    def test_07(self) -> None:
        self.assertEqual(nesting_score("[[[[[[[][]]]]]]][]"), 129)

    def test_08(self) -> None:
        self.assertEqual(nesting_score(""), 0)


if __name__ == "__main__":
    unittest.main()
