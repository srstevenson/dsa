import unittest


# time:  O(9ᵇ * n)
# space: O(9ᵇ * n)
# where: n = len(string), b = number of brace pairs
def decompress_braces(string: str) -> str:
    stack: list[str] = []
    for char in string:
        if char == "}":
            substring: list[str] = []
            while not stack[-1].isdigit():
                substring.append(stack.pop())
            stack.extend(int(stack.pop()) * substring[::-1])
        elif char != "{":
            stack.append(char)

    return "".join(stack)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(decompress_braces("2{q}3{tu}v"), "qqtututuv")

    def test_01(self) -> None:
        self.assertEqual(decompress_braces("ch3{ao}"), "chaoaoao")

    def test_02(self) -> None:
        self.assertEqual(decompress_braces("2{y3{o}}s"), "yoooyooos")

    def test_03(self) -> None:
        self.assertEqual(decompress_braces("z3{a2{xy}b}"), "zaxyxybaxyxybaxyxyb")

    def test_04(self) -> None:
        self.assertEqual(
            decompress_braces("2{3{r4{e}r}io}"),
            "reeeerreeeerreeeerioreeeerreeeerreeeerio",
        )

    def test_05(self) -> None:
        self.assertEqual(
            decompress_braces("go3{spinn2{ing}s}"),
            "gospinningingsspinningingsspinningings",
        )

    def test_06(self) -> None:
        self.assertEqual(decompress_braces("2{l2{if}azu}l"), "lififazulififazul")

    def test_07(self) -> None:
        self.assertEqual(
            decompress_braces("3{al4{ec}2{icia}}"),
            "alececececiciaiciaalececececiciaiciaalececececiciaicia",
        )


if __name__ == "__main__":
    unittest.main()
