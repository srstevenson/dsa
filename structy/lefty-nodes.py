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
def lefty_nodes(root: Node | None) -> list[str]:
    if not root:
        return []

    values: list[str] = []
    queue = deque([(root, 0)])
    while queue:
        current, level = queue.popleft()
        if len(values) == level:
            values.append(current.val)
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))

    return values


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
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
        e.right = h

        self.assertEqual(lefty_nodes(a), ["a", "b", "d", "g"])

    def test_01(self) -> None:
        u = Node("u")
        t = Node("t")
        s = Node("s")
        r = Node("r")
        q = Node("q")
        p = Node("p")

        u.left = t
        u.right = s
        s.right = r
        r.left = q
        r.right = p

        self.assertEqual(lefty_nodes(u), ["u", "t", "r", "q"])

    def test_02(self) -> None:
        l = Node("l")  # noqa: E741
        m = Node("m")
        n = Node("n")
        o = Node("o")
        p = Node("p")
        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")

        l.left = m
        l.right = n
        n.left = o
        n.right = p
        o.left = q
        o.right = r
        p.left = s
        p.right = t

        self.assertEqual(lefty_nodes(l), ["l", "m", "o", "q"])

    def test_03(self) -> None:
        n = Node("n")
        y = Node("y")
        c = Node("c")

        n.left = y
        n.right = c

        self.assertEqual(lefty_nodes(n), ["n", "y"])

    def test_04(self) -> None:
        i = Node("i")
        n = Node("n")
        s = Node("s")
        t = Node("t")

        i.right = n
        n.left = s
        n.right = t

        self.assertEqual(lefty_nodes(i), ["i", "n", "s"])

    def test_05(self) -> None:
        self.assertEqual(lefty_nodes(None), [])


if __name__ == "__main__":
    unittest.main()
