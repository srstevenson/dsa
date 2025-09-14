import unittest


# time:  O(n)
# space: O(n)
# where: n = len(s)
def greet(s: str) -> str:
    return f"hey {s}"


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(greet("alvin"), "hey alvin")

    def test_01(self) -> None:
        self.assertEqual(greet("jason"), "hey jason")

    def test_02(self) -> None:
        self.assertEqual(greet("how now brown cow"), "hey how now brown cow")


if __name__ == "__main__":
    unittest.main()
