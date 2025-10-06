import unittest
from collections import deque


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def breadth_first_values(root: Node | None) -> list[str]:
    if not root:
        return []
    values: list[str] = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

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

        self.assertEqual(breadth_first_values(a), ["a", "b", "c", "d", "e", "f"])

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(
            breadth_first_values(a), ["a", "b", "c", "d", "e", "f", "g", "h"]
        )

    def test_02(self) -> None:
        a = Node("a")

        self.assertEqual(breadth_first_values(a), ["a"])

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        x = Node("x")

        a.right = b
        b.left = c
        c.left = x
        c.right = d
        d.right = e

        self.assertEqual(breadth_first_values(a), ["a", "b", "c", "x", "d", "e"])

    def test_04(self) -> None:
        self.assertEqual(breadth_first_values(None), [])


if __name__ == "__main__":
    unittest.main()
