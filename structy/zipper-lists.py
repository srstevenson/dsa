import unittest


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.next: Node | None = None


# time:  O(min(n, m))
# space: O(1)
# where: n = number of nodes in head_1, m = number of nodes in head_2
def zipper_lists(head_1: Node, head_2: Node) -> Node:
    head = current = head_1
    other = head_2

    while other:
        next_ = current.next
        current.next = other
        current = other
        other = next_

    return head


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[int | str]:
        values: list[int | str] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.next = b
        b.next = c

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z

        self.assertEqual(
            self.values_of(zipper_lists(a, x)), ["a", "x", "b", "y", "c", "z"]
        )

    def test_01(self) -> None:
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

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z

        self.assertEqual(
            self.values_of(zipper_lists(a, x)),
            ["a", "x", "b", "y", "c", "z", "d", "e", "f"],
        )

    def test_02(self) -> None:
        s = Node("s")
        t = Node("t")
        s.next = t

        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        one.next = two
        two.next = three
        three.next = four

        self.assertEqual(self.values_of(zipper_lists(s, one)), ["s", 1, "t", 2, 3, 4])

    def test_03(self) -> None:
        w = Node("w")

        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three

        self.assertEqual(self.values_of(zipper_lists(w, one)), ["w", 1, 2, 3])

    def test_04(self) -> None:
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three

        w = Node("w")

        self.assertEqual(self.values_of(zipper_lists(one, w)), [1, "w", 2, 3])


if __name__ == "__main__":
    unittest.main()
