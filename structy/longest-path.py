import unittest
from functools import cache


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def longest_path(graph: dict[str, list[str]]) -> int:
    @cache
    def _longest_path(node: str) -> int:
        if not graph[node]:
            return 0
        return 1 + max(_longest_path(neighbour) for neighbour in graph[node])

    return max(_longest_path(node) for node in graph)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        graph = {"a": ["c", "b"], "b": ["c"], "c": []}

        self.assertEqual(longest_path(graph), 2)

    def test_01(self) -> None:
        graph = {
            "a": ["c", "b"],
            "b": ["c"],
            "c": [],
            "q": ["r"],
            "r": ["s", "u", "t"],
            "s": ["t"],
            "t": ["u"],
            "u": [],
        }

        self.assertEqual(longest_path(graph), 4)

    def test_02(self) -> None:
        graph = {
            "h": ["i", "j", "k"],
            "g": ["h"],
            "i": [],
            "j": [],
            "k": [],
            "x": ["y"],
            "y": [],
        }

        self.assertEqual(longest_path(graph), 2)

    def test_03(self) -> None:
        graph = {
            "a": ["b"],
            "b": ["c"],
            "c": [],
            "e": ["f"],
            "f": ["g"],
            "g": ["h"],
            "h": [],
        }

        self.assertEqual(longest_path(graph), 3)

    def test_04(self) -> None:
        graph = {
            "a": ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
            "b": ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
            "c": ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
            "d": ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
            "e": ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
            "f": ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
            "g": ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
            "h": ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
            "i": ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
            "j": ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
            "k": ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
            "l": ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"],
            "m": ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"],
            "n": ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            "o": ["p", "q", "r", "s", "t", "u", "v", "w", "x"],
            "p": ["q", "r", "s", "t", "u", "v", "w", "x", "y"],
            "q": ["r", "s", "t", "u", "v", "w", "x", "y"],
            "r": ["s", "t", "u", "v", "w", "x", "y", "z"],
            "s": ["t", "u", "v", "w", "x", "y", "z"],
            "t": ["u", "v", "w", "x", "y", "z"],
            "u": ["v", "w", "x", "y", "z"],
            "v": ["w", "x", "y", "z"],
            "w": ["x", "y", "z"],
            "x": ["y", "z"],
            "y": ["z"],
            "z": [],
        }

        self.assertEqual(longest_path(graph), 25)


if __name__ == "__main__":
    unittest.main()
