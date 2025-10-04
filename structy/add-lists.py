import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(max(n, m))
# space: O(max(n, m))
# where: n = number of nodes in head_1, m = number of nodes in head_2
def add_lists(head_1: Node | None, head_2: Node | None) -> Node | None:
    head = Node(0)

    tail = head
    carry = 0

    while head_1 or head_2:
        val_1 = head_1.val if head_1 else 0
        val_2 = head_2.val if head_2 else 0
        carry, digit = divmod(val_1 + val_2 + carry, 10)
        tail.next = Node(digit)
        tail = tail.next
        if head_1:
            head_1 = head_1.next
        if head_2:
            head_2 = head_2.next

    if carry > 0:
        tail.next = Node(carry)

    return head.next


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[int]:
        values: list[int] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(6)
        a1.next = a2
        a2.next = a3

        b1 = Node(4)
        b2 = Node(5)
        b3 = Node(3)
        b1.next = b2
        b2.next = b3

        self.assertEqual(self.values_of(add_lists(a1, b1)), [5, 7, 9])

    def test_01(self) -> None:
        a1 = Node(1)
        a2 = Node(4)
        a3 = Node(5)
        a4 = Node(7)
        a1.next = a2
        a2.next = a3
        a3.next = a4

        b1 = Node(2)
        b2 = Node(3)
        b1.next = b2

        self.assertEqual(self.values_of(add_lists(a1, b1)), [3, 7, 5, 7])

    def test_02(self) -> None:
        a1 = Node(9)
        a2 = Node(3)
        a1.next = a2

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2

        self.assertEqual(self.values_of(add_lists(a1, b1)), [6, 8])

    def test_03(self) -> None:
        a1 = Node(9)
        a2 = Node(8)
        a1.next = a2

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2

        self.assertEqual(self.values_of(add_lists(a1, b1)), [6, 3, 1])

    def test_04(self) -> None:
        a1 = Node(9)
        a2 = Node(9)
        a3 = Node(9)
        a1.next = a2
        a2.next = a3

        b1 = Node(6)

        self.assertEqual(self.values_of(add_lists(a1, b1)), [5, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
