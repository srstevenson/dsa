import unittest


# time:  O(n)
# space: O(n)
# where: n = len(s)
def compress(s: str) -> str:
    compressed: list[str] = []
    i = j = 0
    while i < len(s):
        while j < len(s) and s[j] == s[i]:
            j += 1
        if (count := j - i) > 1:
            compressed.append(str(count))
        compressed.append(s[i])
        i = j

    return "".join(compressed)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(compress("ccaaatsss"), "2c3at3s")

    def test_01(self) -> None:
        self.assertEqual(compress("ssssbbz"), "4s2bz")

    def test_02(self) -> None:
        self.assertEqual(compress("ppoppppp"), "2po5p")

    def test_03(self) -> None:
        self.assertEqual(compress("nnneeeeeeeeeeeezz"), "3n12e2z")

    def test_04(self) -> None:
        self.assertEqual(
            compress(
                "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
            ),
            "127y",
        )


if __name__ == "__main__":
    unittest.main()
