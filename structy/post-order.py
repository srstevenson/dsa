import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def post_order(root: Node | None) -> list[str]:
    values: list[str] = []
    _post_order(root, values)
    return values


def _post_order(root: Node | None, values: list[str]) -> None:
    if root:
        _post_order(root.left, values)
        _post_order(root.right, values)
        values.append(root.val)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.left = y
        x.right = z

        self.assertEqual(post_order(x), ["y", "z", "x"])

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
        c.left = f
        c.right = g

        self.assertEqual(post_order(a), ["d", "e", "b", "f", "g", "c", "a"])

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

        self.assertEqual(post_order(a), ["d", "g", "h", "e", "b", "f", "c", "a"])

    def test_03(self) -> None:
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

        self.assertEqual(post_order(l), ["m", "q", "r", "o", "s", "t", "p", "n", "l"])

    def test_04(self) -> None:
        self.assertEqual(post_order(None), [])


if __name__ == "__main__":
    unittest.main()
