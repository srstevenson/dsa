import unittest


# time:  O(n)
# space: O(n)
# where: n = len(s)
def token_replace(s: str, tokens: dict[str, str]) -> str:
    result: list[str] = []
    i = 0
    j = 1
    while i < len(s):
        if s[i] != "$":
            result.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != "$":
            j += 1
        else:
            result.append(tokens[s[i : j + 1]])
            i = j + 1
            j = i + 1

    return "".join(result)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        tokens = {"$LOCATION$": "park", "$ANIMAL$": "dog"}
        self.assertEqual(
            token_replace("Walk the $ANIMAL$ in the $LOCATION$!", tokens),
            "Walk the dog in the park!",
        )

    def test_01(self) -> None:
        tokens = {"$ADJECTIVE$": "quick", "$VERB$": "hopped", "$DIRECTION$": "North"}
        self.assertEqual(
            token_replace(
                "the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward", tokens
            ),
            "the quick fox hopped quickly Northward",
        )

    def test_02(self) -> None:
        tokens = {"$greeting$": "hey programmer"}
        self.assertEqual(
            token_replace("his greeting is always $greeting$.", tokens),
            "his greeting is always hey programmer.",
        )

    def test_03(self) -> None:
        tokens = {"$A$": "lions", "$B$": "tigers", "$C$": "bears"}
        self.assertEqual(
            token_replace("$A$$B$$C$, oh my.", tokens), "lionstigersbears, oh my."
        )

    def test_04(self) -> None:
        tokens = {"$A$": "lions", "$B$": "tigers", "$C$": "bears"}
        self.assertEqual(token_replace("$B$", tokens), "tigers")

    def test_05(self) -> None:
        tokens = {"$second$": "beta", "$first$": "alpha", "$third$": "gamma"}
        self.assertEqual(
            token_replace("$first$second$third$", tokens), "alphasecondgamma"
        )


if __name__ == "__main__":
    unittest.main()
