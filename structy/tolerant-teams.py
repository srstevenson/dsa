import unittest
from collections import defaultdict


# time:  O(n + e)
# space: O(n + e)
# where: n = number of nodes, e = number of edges
def tolerant_teams(rivalries: list[tuple[str, str]]) -> bool:
    graph: defaultdict[str, list[str]] = defaultdict(list)
    for a, b in rivalries:
        graph[a].append(b)
        graph[b].append(a)

    colors: dict[str, bool] = {}

    for person in graph:
        if person in colors:
            continue

        colors[person] = True
        stack = [person]

        while stack:
            current = stack.pop()
            for rival in graph[current]:
                if rival in colors:
                    if colors[rival] == colors[current]:
                        return False
                else:
                    colors[rival] = not colors[current]
                    stack.append(rival)

    return True


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(tolerant_teams([("philip", "seb"), ("raj", "nader")]))

    def test_01(self) -> None:
        self.assertFalse(
            tolerant_teams(
                [("philip", "seb"), ("raj", "nader"), ("raj", "philip"), ("seb", "raj")]
            )
        )

    def test_02(self) -> None:
        self.assertTrue(
            tolerant_teams(
                [
                    ("cindy", "anj"),
                    ("alex", "matt"),
                    ("alex", "cindy"),
                    ("anj", "matt"),
                    ("brando", "matt"),
                ]
            )
        )

    def test_03(self) -> None:
        self.assertFalse(
            tolerant_teams(
                [
                    ("alex", "anj"),
                    ("alex", "matt"),
                    ("alex", "cindy"),
                    ("anj", "matt"),
                    ("brando", "matt"),
                ]
            )
        )

    def test_04(self) -> None:
        self.assertTrue(
            tolerant_teams(
                [
                    ("alan", "jj"),
                    ("betty", "richard"),
                    ("jj", "simcha"),
                    ("richard", "christine"),
                ]
            )
        )

    def test_05(self) -> None:
        self.assertTrue(
            tolerant_teams(
                [
                    ("alan", "jj"),
                    ("jj", "richard"),
                    ("betty", "richard"),
                    ("jj", "simcha"),
                    ("richard", "christine"),
                ]
            )
        )

    def test_06(self) -> None:
        self.assertFalse(
            tolerant_teams(
                [
                    ("alan", "jj"),
                    ("betty", "richard"),
                    ("betty", "christine"),
                    ("jj", "simcha"),
                    ("richard", "christine"),
                ]
            )
        )

    def test_07(self) -> None:
        self.assertTrue(
            tolerant_teams([("ara", "boyka"), ("dennis", "clara"), ("boyka", "clara")])
        )


if __name__ == "__main__":
    unittest.main()
