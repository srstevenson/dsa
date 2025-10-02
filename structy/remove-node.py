import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def remove_node(head: Node, target_val: str) -> Node | None:
    if head.val == target_val:
        return head.next

    previous = head
    current = head.next
    while current:
        if current.val == target_val:
            previous.next = current.next
            return head
        previous = current
        current = current.next


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[str]:
        values: list[str] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual(self.values_of(remove_node(a, "c")), ["a", "b", "d", "e", "f"])

    def test_01(self) -> None:
        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z

        self.assertEqual(self.values_of(remove_node(x, "z")), ["x", "y"])

    def test_02(self) -> None:
        q = Node("q")
        r = Node("r")
        s = Node("s")

        q.next = r
        r.next = s

        self.assertEqual(self.values_of(remove_node(q, "q")), ["r", "s"])

    def test_03(self) -> None:
        node1 = Node("h")
        node2 = Node("i")
        node3 = Node("j")
        node4 = Node("i")

        node1.next = node2
        node2.next = node3
        node3.next = node4

        self.assertEqual(self.values_of(remove_node(node1, "i")), ["h", "j", "i"])

    def test_04(self) -> None:
        t = Node("t")

        self.assertIsNone(remove_node(t, "t"))


if __name__ == "__main__":
    unittest.main()
