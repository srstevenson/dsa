import itertools
import unittest


# time:  O(c n! / (n - c)!)
# space: O(c n! / (n - c)!)
# where: n = len(people), c = capacity
def lining_up(people: list[str], capacity: int) -> list[list[str]]:
    result: list[list[str]] = []
    current: list[str] = []
    used = [False for _ in people]

    def _backtrack() -> None:
        if len(current) == capacity:
            result.append(current[:])
            return

        for idx in range(len(people)):
            if used[idx]:
                continue
            current.append(people[idx])
            used[idx] = True
            _backtrack()
            current.pop()
            used[idx] = False

    _backtrack()
    return result


# time:  O(c n! / (n - c)!)
# space: O(c n! / (n - c)!)
# where: n = len(people), c = capacity
def lining_up_itertools(people: list[str], capacity: int) -> list[list[str]]:
    return list(map(list, itertools.permutations(people, capacity)))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [lining_up, lining_up_itertools]:
            self.assertCountEqual(
                solution(["jason", "jen", "cody", "vicky"], 3),
                [
                    ["jason", "jen", "cody"],
                    ["jen", "jason", "cody"],
                    ["jen", "cody", "jason"],
                    ["jason", "cody", "jen"],
                    ["cody", "jason", "jen"],
                    ["cody", "jen", "jason"],
                    ["jason", "jen", "vicky"],
                    ["jen", "jason", "vicky"],
                    ["jen", "vicky", "jason"],
                    ["jason", "vicky", "jen"],
                    ["vicky", "jason", "jen"],
                    ["vicky", "jen", "jason"],
                    ["jason", "cody", "vicky"],
                    ["cody", "jason", "vicky"],
                    ["cody", "vicky", "jason"],
                    ["jason", "vicky", "cody"],
                    ["vicky", "jason", "cody"],
                    ["vicky", "cody", "jason"],
                    ["jen", "cody", "vicky"],
                    ["cody", "jen", "vicky"],
                    ["cody", "vicky", "jen"],
                    ["jen", "vicky", "cody"],
                    ["vicky", "jen", "cody"],
                    ["vicky", "cody", "jen"],
                ],
            )

    def test_01(self) -> None:
        for solution in [lining_up, lining_up_itertools]:
            self.assertCountEqual(
                solution(["autumn", "anj", "aud"], 2),
                [
                    ["autumn", "anj"],
                    ["anj", "autumn"],
                    ["autumn", "aud"],
                    ["aud", "autumn"],
                    ["anj", "aud"],
                    ["aud", "anj"],
                ],
            )

    def test_02(self) -> None:
        for solution in [lining_up, lining_up_itertools]:
            self.assertCountEqual(
                solution(["anj", "aud"], 2), [["anj", "aud"], ["aud", "anj"]]
            )

    def test_03(self) -> None:
        for solution in [lining_up, lining_up_itertools]:
            self.assertCountEqual(solution(["anj", "aud"], 1), [["anj"], ["aud"]])


if __name__ == "__main__":
    unittest.main()
