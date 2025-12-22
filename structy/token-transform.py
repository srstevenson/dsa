import unittest
from functools import cache


# time:  O(n + ml)
# space: O(n + ml)
# where: n = len(s), m = len(tokens), l = length of longest token
def token_transform(s: str, tokens: dict[str, str]) -> str:
    @cache
    def _token_transform(s: str) -> str:
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
                result.append(_token_transform(tokens[s[i : j + 1]]))
                i = j + 1
                j = i + 1

        return "".join(result)

    return _token_transform(s)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        tokens = {"$LOCATION$": "$ANIMAL$ park", "$ANIMAL$": "dog"}
        self.assertEqual(
            token_transform("Walk the $ANIMAL$ in the $LOCATION$!", tokens),
            "Walk the dog in the dog park!",
        )

    def test_01(self) -> None:
        tokens = {
            "$ADJECTIVE_1$": "quick",
            "$ADJECTIVE_2$": "eager",
            "$ADVERBS$": "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
            "$VERB$": "hopped $DIRECTION$",
            "$DIRECTION$": "North",
        }
        self.assertEqual(
            token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens),
            "the quick fox quickly and eagerly hopped Northward",
        )

    def test_02(self) -> None:
        tokens = {
            "$B$": "epicly $C$",
            "$A$": "pretty $B$ problem $D$",
            "$D$": "we have",
            "$C$": "clever",
        }
        self.assertEqual(
            token_transform("What a $A$ here!", tokens),
            "What a pretty epicly clever problem we have here!",
        )

    def test_03(self) -> None:
        tokens = {
            "$1$": "a$2$",
            "$2$": "b$3$",
            "$3$": "c$4$",
            "$4$": "d$5$",
            "$5$": "e$6$",
            "$6$": "f!",
        }
        self.assertEqual(
            token_transform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens),
            "abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!",
        )

    def test_04(self) -> None:
        tokens = {
            "$0$": "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
            "$1$": "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
            "$2$": "$3$$3$$3$$3$$3$$3$$3$",
            "$3$": "$4$$4$$4$$4$$4$$4$",
            "$4$": "$5$$5$$5$$5$$5$",
            "$5$": "$6$$6$$6$$6$",
            "$6$": "$7$$7$$7$",
            "$7$": "$8$$8$",
            "$8$": "",
        }
        self.assertEqual(
            token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens), "zzzzzzz"
        )


if __name__ == "__main__":
    unittest.main()
