import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def flip_tree(root: Node | None) -> Node | None:
    if root:
        root.left, root.right = flip_tree(root.right), flip_tree(root.left)
    return root


class TestSolution(unittest.TestCase):
    def values_of(self, root: Node) -> list[str]:
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

        flip_tree(a)

        self.assertEqual(self.values_of(a), ["a", "c", "f", "b", "e", "h", "g", "d"])

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

        flip_tree(u)

        self.assertEqual(self.values_of(u), ["u", "s", "r", "p", "q", "t"])

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

        flip_tree(l)

        self.assertEqual(
            self.values_of(l), ["l", "n", "p", "t", "s", "o", "r", "q", "m"]
        )

    def test_03(self) -> None:
        n = Node("n")
        y = Node("y")
        c = Node("c")

        n.left = y
        n.right = c

        flip_tree(n)

        self.assertEqual(self.values_of(n), ["n", "c", "y"])


if __name__ == "__main__":
    unittest.main()
