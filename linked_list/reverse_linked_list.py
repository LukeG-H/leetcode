#!/usr/bin/python3

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, values: list[int] | None = None) -> None:
        self.head: Node | None = None
        if values:
            # Preserve input order: [1,2,3] becomes 1->2->3->None instead of 3->2->1->None
            for val in reversed(values):
                self.push(val)

    def push(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end=" ")
            curr = curr.next
        print("\n")

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev


class Solution:
    def solve(self, num_list: list[int]):
        # num_list added in order
        llist = LinkedList(num_list) 

        print("Given Linked list:")
        llist.print_list()

        # new vals will be added to front of linked list
        print("Adding new values to the FRONT of the list:")
        for i in range(5, 0, -1):
            print(f"Pushing {i} to front of list...")
            llist.push(i)
            llist.print_list()

        # reverse the list
        llist.reverse()
        print("Reversed Linked list:")
        llist.print_list()


def main():
    tests = {
        1: {"nums": [6, 7, 8, 9, 10]},
        2: {"nums": [1, 2, 3, 4, 5]},
        3: {"nums": [-1, 0, 3, 7, 10]},
    }

    ans1 = Solution().solve(tests[1]["nums"])
    ans2 = Solution().solve(tests[2]["nums"])
    ans3 = Solution().solve(tests[3]["nums"])



if __name__ == '__main__':
    main()

