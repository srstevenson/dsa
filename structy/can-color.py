import unittest


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def can_color(graph: dict[str, list[str]]) -> bool:
    colors: dict[str, bool] = {}

    for node in graph:
        if node in colors:
            continue

        colors[node] = True
        stack = [node]

        while stack:
            current = stack.pop()
            for neighbour in graph[current]:
                if neighbour in colors:
                    if colors[neighbour] == colors[current]:
                        return False
                else:
                    colors[neighbour] = not colors[current]
                    stack.append(neighbour)

    return True


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(can_color({"x": ["y"], "y": ["x", "z"], "z": ["y"]}))

    def test_01(self) -> None:
        self.assertFalse(can_color({"q": ["r", "s"], "r": ["q", "s"], "s": ["r", "q"]}))

    def test_02(self) -> None:
        self.assertTrue(
            can_color({"a": ["b", "c", "d"], "b": ["a"], "c": ["a"], "d": ["a"]})
        )

    def test_03(self) -> None:
        self.assertFalse(
            can_color(
                {"a": ["b", "c", "d"], "b": ["a"], "c": ["a", "d"], "d": ["a", "c"]}
            )
        )

    def test_04(self) -> None:
        self.assertTrue(
            can_color(
                {"h": ["i", "k"], "i": ["h", "j"], "j": ["i", "k"], "k": ["h", "j"]}
            )
        )

    def test_05(self) -> None:
        self.assertTrue(can_color({"z": []}))

    def test_06(self) -> None:
        self.assertFalse(
            can_color(
                {
                    "h": ["i", "k"],
                    "i": ["h", "j"],
                    "j": ["i", "k"],
                    "k": ["h", "j"],
                    "q": ["r", "s"],
                    "r": ["q", "s"],
                    "s": ["r", "q"],
                }
            )
        )

    def test_07(self) -> None:
        self.assertTrue(
            can_color(
                {
                    "a": ["b", "d"],
                    "c": ["b", "f"],
                    "b": ["a", "c"],
                    "d": ["a", "e"],
                    "e": ["d", "f"],
                    "f": ["e", "c"],
                }
            )
        )

    def test_08(self) -> None:
        self.assertTrue(
            can_color({"a": ["b"], "d": ["c"], "b": ["a", "c"], "c": ["b", "d"]})
        )


if __name__ == "__main__":
    unittest.main()
