import unittest


# time:  O(n + e)
# space: O(n)
# where: n = num_courses, e = len(prereqs)
def prereqs_possible(num_courses: int, prereqs: list[tuple[int, int]]) -> bool:
    graph: dict[int, list[int]] = {course: [] for course in range(num_courses)}
    for dep, course in prereqs:
        graph[course].append(dep)

    visited: set[int] = set()
    visiting: set[int] = set()
    for course in graph:
        if _contains_cycle(graph, visited, visiting, course):
            return False
    return True


def _contains_cycle(
    graph: dict[int, list[int]], visited: set[int], visiting: set[int], course: int
) -> bool:
    if course in visited:
        return False
    if course in visiting:
        return True
    visiting.add(course)
    for dep in graph[course]:
        if _contains_cycle(graph, visited, visiting, dep):
            return True
    visiting.remove(course)
    visited.add(course)
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        num_courses = 6
        prereqs = [(0, 1), (2, 3), (0, 2), (1, 3), (4, 5)]
        self.assertTrue(prereqs_possible(num_courses, prereqs))

    def test_01(self) -> None:
        num_courses = 6
        prereqs = [(0, 1), (2, 3), (0, 2), (1, 3), (4, 5), (3, 0)]
        self.assertFalse(prereqs_possible(num_courses, prereqs))

    def test_02(self) -> None:
        num_courses = 5
        prereqs = [(2, 4), (1, 0), (0, 2), (0, 4)]
        self.assertTrue(prereqs_possible(num_courses, prereqs))

    def test_03(self) -> None:
        num_courses = 6
        prereqs = [(2, 4), (1, 0), (0, 2), (0, 4), (5, 3), (3, 5)]
        self.assertFalse(prereqs_possible(num_courses, prereqs))

    def test_04(self) -> None:
        num_courses = 8
        prereqs = [(1, 0), (0, 6), (2, 0), (0, 5), (3, 7), (4, 3)]
        self.assertTrue(prereqs_possible(num_courses, prereqs))

    def test_05(self) -> None:
        num_courses = 8
        prereqs = [(1, 0), (0, 6), (2, 0), (0, 5), (3, 7), (7, 4), (4, 3)]
        self.assertFalse(prereqs_possible(num_courses, prereqs))

    def test_06(self) -> None:
        num_courses = 42
        prereqs = [(6, 36)]
        self.assertTrue(prereqs_possible(num_courses, prereqs))


if __name__ == "__main__":
    unittest.main()
