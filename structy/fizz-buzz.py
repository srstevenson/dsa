import unittest


# time:  O(n)
# space: O(n)
def fizz_buzz(n: int) -> list[int | str]:
    result: list[int | str] = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append("fizzbuzz")
        elif i % 5 == 0:
            result.append("buzz")
        elif i % 3 == 0:
            result.append("fizz")
        else:
            result.append(i)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            fizz_buzz(11), [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]
        )

    def test_01(self) -> None:
        self.assertEqual(fizz_buzz(2), [1, 2])

    def test_02(self) -> None:
        self.assertEqual(
            fizz_buzz(16),
            [
                1,
                2,
                "fizz",
                4,
                "buzz",
                "fizz",
                7,
                8,
                "fizz",
                "buzz",
                11,
                "fizz",
                13,
                14,
                "fizzbuzz",
                16,
            ],
        )

    def test_03(self) -> None:
        self.assertEqual(
            fizz_buzz(32),
            [
                1,
                2,
                "fizz",
                4,
                "buzz",
                "fizz",
                7,
                8,
                "fizz",
                "buzz",
                11,
                "fizz",
                13,
                14,
                "fizzbuzz",
                16,
                17,
                "fizz",
                19,
                "buzz",
                "fizz",
                22,
                23,
                "fizz",
                "buzz",
                26,
                "fizz",
                28,
                29,
                "fizzbuzz",
                31,
                32,
            ],
        )


if __name__ == "__main__":
    unittest.main()
