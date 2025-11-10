import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def lowest_common_ancestor(root: Node | None, val1: str, val2: str) -> str | None:
    if not root:
        return None

    if root.val in (val1, val2):
        return root.val

    left = lowest_common_ancestor(root.left, val1, val2)
    right = lowest_common_ancestor(root.right, val1, val2)

    if left and right:
        return root.val

    return left if left else right


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

        self.assertEqual(lowest_common_ancestor(a, "d", "h"), "b")

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
        e.right = h

        self.assertEqual(lowest_common_ancestor(a, "d", "g"), "b")

    def test_02(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(a, "g", "c"), "a")

    def test_03(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(a, "b", "g"), "b")

    def test_04(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(a, "f", "c"), "c")

    def test_05(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(l, "r", "p"), "n")

    def test_06(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(l, "m", "o"), "l")

    def test_07(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(l, "t", "q"), "n")

    def test_08(self) -> None:
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

        self.assertEqual(lowest_common_ancestor(l, "s", "p"), "p")


if __name__ == "__main__":
    unittest.main()
