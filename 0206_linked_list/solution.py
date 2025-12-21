#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        return head

    def create_nodes(self, values: list[int]) -> list[ListNode]:
        nodes = []
        for val in values:
            nodes.append(ListNode(val))
        return nodes

    def link_nodes(self, nodes: list[ListNode]) -> ListNode:
        head = nodes[0]
        for i in range(len(nodes) - 1):  #skip the last index as that node's 'next' will be None
            nodes[i].next = nodes[i+1]
        return head

    def create_linked_list(self, values: list[int]) -> ListNode | None:
        head = None
        for val in reversed(values):
            node = ListNode(val)
            node.next = head
            head = node
        return head

    def print_linked_list(self, head: ListNode | None) -> None:
        current = head
        while current:
            print(f"{current.val} ->", end=" ")
            current = current.next
        print("\n")


if __name__ == '__main__':
    values = [1,2,3,4,5]
    solution = Solution()
    nodes = solution.create_nodes(values)
    head = solution.link_nodes(nodes)
    solution.print_linked_list(head)
    new_head = solution.reverseList(head)
    solution.print_linked_list(new_head)

    solution2 = Solution()
    head2 = solution2.create_linked_list(values)
    solution2.print_linked_list(head2)
    new_head2 = Solution().reverseList(head2)
    solution2.print_linked_list(new_head)
