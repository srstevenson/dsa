import unittest
from functools import cache


# time:  O(n + e)
# space: O(n)
# where: n = num_courses, e = len(prereqs)
def semesters_required(num_courses: int, prereqs: list[tuple[int, int]]) -> int:
    graph: dict[int, list[int]] = {course: [] for course in range(num_courses)}
    for course, dep in prereqs:
        graph[course].append(dep)

    @cache
    def _semesters_required(course: int) -> int:
        if not graph[course]:
            return 1
        return 1 + max(_semesters_required(neighbour) for neighbour in graph[course])

    return max(_semesters_required(course) for course in graph)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        num_courses = 6
        prereqs = [(1, 2), (2, 4), (3, 5), (0, 5)]
        self.assertEqual(semesters_required(num_courses, prereqs), 3)

    def test_01(self) -> None:
        num_courses = 7
        prereqs = [(4, 3), (3, 2), (2, 1), (1, 0), (5, 2), (5, 6)]
        self.assertEqual(semesters_required(num_courses, prereqs), 5)

    def test_02(self) -> None:
        num_courses = 5
        prereqs = [(1, 0), (3, 4), (1, 2), (3, 2)]
        self.assertEqual(semesters_required(num_courses, prereqs), 2)

    def test_03(self) -> None:
        num_courses = 12
        prereqs: list[tuple[int, int]] = []
        self.assertEqual(semesters_required(num_courses, prereqs), 1)

    def test_04(self) -> None:
        num_courses = 3
        prereqs = [(0, 2), (0, 1), (1, 2)]
        self.assertEqual(semesters_required(num_courses, prereqs), 3)

    def test_05(self) -> None:
        num_courses = 6
        prereqs = [(3, 4), (3, 0), (3, 1), (3, 2), (3, 5)]
        self.assertEqual(semesters_required(num_courses, prereqs), 2)


if __name__ == "__main__":
    unittest.main()
