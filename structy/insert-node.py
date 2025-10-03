import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def insert_node(head: Node, value: str, index: int) -> Node | None:
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    current = head
    current_index = 0

    while current:
        if current_index == index - 1:
            next_ = current.next
            current.next = Node(value)
            current.next.next = next_
            return head

        current = current.next
        current_index += 1


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

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(
            self.values_of(insert_node(a, "x", 2)), ["a", "b", "x", "c", "d"]
        )

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(
            self.values_of(insert_node(a, "v", 3)), ["a", "b", "c", "v", "d"]
        )

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(
            self.values_of(insert_node(a, "m", 4)), ["a", "b", "c", "d", "m"]
        )

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")

        a.next = b

        self.assertEqual(self.values_of(insert_node(a, "z", 0)), ["z", "a", "b"])


if __name__ == "__main__":
    unittest.main()
