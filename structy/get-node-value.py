import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def get_node_value(head: Node, index: int) -> str | None:
    current = head
    current_idx = 0
    while current:
        if current_idx == index:
            return current.val
        current = current.next
        current_idx += 1
    return None


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(get_node_value(a, 2), "c")

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(get_node_value(a, 3), "d")

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertIsNone(get_node_value(a, 7))

    def test_03(self) -> None:
        node1 = Node("banana")
        node2 = Node("mango")

        node1.next = node2

        self.assertEqual(get_node_value(node1, 0), "banana")

    def test_04(self) -> None:
        node1 = Node("banana")
        node2 = Node("mango")

        node1.next = node2

        self.assertEqual(get_node_value(node1, 1), "mango")


if __name__ == "__main__":
    unittest.main()
