import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n log n)
# space: O(n log n)
# where: n = number of nodes
def all_tree_paths(root: Node) -> list[list[str]]:
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()
    return paths


def _all_tree_paths(root: Node | None) -> list[list[str]]:
    if not root:
        return []

    if not root.left and not root.right:
        return [[root.val]]

    paths = _all_tree_paths(root.left)
    paths.extend(_all_tree_paths(root.right))
    for path in paths:
        path.append(root.val)
    return paths


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

        self.assertEqual(
            all_tree_paths(a), [["a", "b", "d"], ["a", "b", "e"], ["a", "c", "f"]]
        )

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
            all_tree_paths(a),
            [
                ["a", "b", "d"],
                ["a", "b", "e", "g"],
                ["a", "b", "e", "h"],
                ["a", "c", "f", "i"],
            ],
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

        self.assertEqual(all_tree_paths(q), [["q", "r", "t", "u", "v"], ["q", "s"]])

    def test_03(self) -> None:
        z = Node("z")

        self.assertEqual(all_tree_paths(z), [["z"]])


if __name__ == "__main__":
    unittest.main()
