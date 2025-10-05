import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def depth_first_values(root: Node | None) -> list[str]:
    if not root:
        return []

    values: list[str] = []
    stack = [root]

    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return values


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def depth_first_values_recursive(root: Node | None) -> list[str]:
    values: list[str] = []
    if root:
        values.append(root.val)
        values.extend(depth_first_values_recursive(root.left))
        values.extend(depth_first_values_recursive(root.right))
    return values


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        for solution in [depth_first_values, depth_first_values_recursive]:
            self.assertEqual(solution(a), ["a", "b", "d", "e", "c", "f"])

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        for solution in [depth_first_values, depth_first_values_recursive]:
            self.assertEqual(solution(a), ["a", "b", "d", "e", "g", "c", "f"])

    def test_02(self) -> None:
        a = Node("a")

        for solution in [depth_first_values, depth_first_values_recursive]:
            self.assertEqual(solution(a), ["a"])

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        for solution in [depth_first_values, depth_first_values_recursive]:
            self.assertEqual(solution(a), ["a", "b", "c", "d", "e"])

    def test_04(self) -> None:
        for solution in [depth_first_values, depth_first_values_recursive]:
            self.assertEqual(solution(None), [])


if __name__ == "__main__":
    unittest.main()
