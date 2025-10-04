import unittest


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = len(values)
def create_linked_list(values: list[int] | list[str]) -> Node | None:
    head = Node("")
    current = head

    for value in values:
        current.next = Node(value)
        current = current.next

    return head.next


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[int | str]:
        values: list[int | str] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        values = ["h", "e", "y"]
        self.assertEqual(self.values_of(create_linked_list(values)), values)

    def test_01(self) -> None:
        values = [1, 7, 1, 8]
        self.assertEqual(self.values_of(create_linked_list(values)), values)

    def test_02(self) -> None:
        values = ["a"]
        self.assertEqual(self.values_of(create_linked_list(values)), values)

    def test_03(self) -> None:
        self.assertIsNone(create_linked_list([]))


if __name__ == "__main__":
    unittest.main()
