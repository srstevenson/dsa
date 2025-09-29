import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def reverse_list(head: Node) -> Node | None:
    current = head
    prev = None
    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def reverse_list_recursive(head: Node | None, prev: Node | None = None) -> Node | None:
    if not head:
        return prev
    next_ = head.next
    head.next = prev
    return reverse_list_recursive(next_, head)


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[str]:
        values: list[str] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        for solution in [reverse_list, reverse_list_recursive]:
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

            self.assertEqual(
                self.values_of(solution(a)), ["f", "e", "d", "c", "b", "a"]
            )

    def test_01(self) -> None:
        for solution in [reverse_list, reverse_list_recursive]:
            x = Node("x")
            y = Node("y")

            x.next = y

            self.assertEqual(self.values_of(solution(x)), ["y", "x"])

    def test_02(self) -> None:
        for solution in [reverse_list, reverse_list_recursive]:
            p = Node("p")

            self.assertEqual(self.values_of(solution(p)), ["p"])


if __name__ == "__main__":
    unittest.main()
