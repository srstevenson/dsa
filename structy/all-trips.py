import unittest
from collections import defaultdict


# time:  O(2ⁿn)
# space: O(2ⁿn)
# where: n = number of nodes
def all_trips(
    routes: list[tuple[str, str]], start_station: str, end_station: str
) -> list[list[str]]:
    graph: defaultdict[str, list[str]] = defaultdict(list)
    for start, end in routes:
        graph[start].append(end)

    result: list[list[str]] = []
    route = [start_station]

    def _backtrack(start_station: str) -> None:
        if start_station == end_station:
            result.append(route[:])
            return

        for neighbour in graph[start_station]:
            route.append(neighbour)
            _backtrack(neighbour)
            route.pop()

    _backtrack(start_station)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        routes = [
            ("brookdale", "denton junction"),
            ("astor place", "brookdale"),
            ("astor place", "cony island"),
            ("astor place", "denton junction"),
            ("cony island", "denton junction"),
        ]
        self.assertCountEqual(
            all_trips(routes, "astor place", "denton junction"),
            [
                ["astor place", "brookdale", "denton junction"],
                ["astor place", "cony island", "denton junction"],
                ["astor place", "denton junction"],
            ],
        )

    def test_01(self) -> None:
        routes = [
            ("brookdale", "denton junction"),
            ("astor place", "brookdale"),
            ("astor place", "cony island"),
            ("astor place", "denton junction"),
            ("cony island", "denton junction"),
        ]
        self.assertEqual(all_trips(routes, "cony island", "brookdale"), [])

    def test_02(self) -> None:
        routes = [
            ("arlington", "boerum"),
            ("boerum", "central"),
            ("central", "euclid"),
            ("euclid", "fairfax"),
            ("arlington", "dyckman"),
            ("boerum", "euclid"),
            ("dyckman", "boerum"),
            ("dyckman", "fairfax"),
        ]
        self.assertCountEqual(
            all_trips(routes, "arlington", "central"),
            [
                ["arlington", "boerum", "central"],
                ["arlington", "dyckman", "boerum", "central"],
            ],
        )

    def test_03(self) -> None:
        routes = [
            ("arlington", "boerum"),
            ("boerum", "central"),
            ("central", "euclid"),
            ("euclid", "fairfax"),
            ("arlington", "dyckman"),
            ("boerum", "euclid"),
            ("dyckman", "boerum"),
            ("dyckman", "fairfax"),
        ]
        self.assertCountEqual(
            all_trips(routes, "arlington", "fairfax"),
            [
                ["arlington", "boerum", "central", "euclid", "fairfax"],
                ["arlington", "boerum", "euclid", "fairfax"],
                ["arlington", "dyckman", "boerum", "central", "euclid", "fairfax"],
                ["arlington", "dyckman", "boerum", "euclid", "fairfax"],
                ["arlington", "dyckman", "fairfax"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
