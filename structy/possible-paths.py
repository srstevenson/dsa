import unittest


# time:  O(2ⁿn)
# space: O(2ⁿn)
# where: n = len(graph)
def possible_paths(graph: dict[str, list[str]], src: str, dst: str) -> list[list[str]]:
    result: list[list[str]] = []
    path = [src]

    def _backtrack(current: str) -> None:
        if current == dst:
            result.append(path[:])
            return

        for neighbour in graph[current]:
            path.append(neighbour)
            _backtrack(neighbour)
            path.pop()

    _backtrack(src)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        graph = {"a": ["b", "c", "d"], "b": ["d"], "c": ["d"], "d": []}
        self.assertCountEqual(
            possible_paths(graph, "a", "d"),
            [["a", "b", "d"], ["a", "c", "d"], ["a", "d"]],
        )

    def test_01(self) -> None:
        graph = {"a": ["b", "c", "d"], "b": ["d"], "c": ["d"], "d": []}
        self.assertEqual(possible_paths(graph, "c", "b"), [])

    def test_02(self) -> None:
        graph = {
            "a": ["b", "d"],
            "b": ["c", "e"],
            "c": ["e"],
            "d": ["b", "f"],
            "e": ["f"],
            "f": [],
        }
        self.assertCountEqual(
            possible_paths(graph, "a", "c"), [["a", "b", "c"], ["a", "d", "b", "c"]]
        )

    def test_03(self) -> None:
        graph = {
            "a": ["b", "d"],
            "b": ["c", "e"],
            "c": ["e"],
            "d": ["b", "f"],
            "e": ["f"],
            "f": [],
        }
        self.assertCountEqual(
            possible_paths(graph, "a", "f"),
            [
                ["a", "b", "c", "e", "f"],
                ["a", "b", "e", "f"],
                ["a", "d", "b", "c", "e", "f"],
                ["a", "d", "b", "e", "f"],
                ["a", "d", "f"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
