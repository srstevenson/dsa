import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def leaf_layers(root: Node | None) -> list[list[str]]:
    layers: list[list[str]] = []

    def _height(root: Node | None) -> int:
        if not root:
            return -1

        height = 1 + max(_height(root.left), _height(root.right))

        if len(layers) > height:
            layers[height].append(root.val)
        else:
            layers.append([root.val])

        return height

    _height(root)
    return layers


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

        self.assertEqual(leaf_layers(a), [["d", "e", "f"], ["b", "c"], ["a"]])

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        self.assertEqual(
            leaf_layers(a), [["d", "g", "h", "i"], ["e", "f"], ["b", "c"], ["a"]]
        )

    def test_02(self) -> None:
        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")
        v = Node("v")

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        self.assertEqual(leaf_layers(q), [["v", "s"], ["u"], ["t"], ["r"], ["q"]])

    def test_03(self) -> None:
        self.assertEqual(leaf_layers(None), [])

    def test_04(self) -> None:
        a = Node("x")
        b = Node("x")
        c = Node("x")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("x")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        self.assertEqual(
            leaf_layers(a), [["d", "g", "h", "x"], ["e", "f"], ["x", "x"], ["x"]]
        )


if __name__ == "__main__":
    unittest.main()
