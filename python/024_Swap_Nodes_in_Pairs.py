"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
        
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     cur = dummy

    #     while cur.next and cur.next.next:
    #         first = cur.next
    #         second = cur.next.next

    #         cur.next = second

    #         first.next = second.next
    #         second.next = first
    #         cur = cur.next.next
        
    #     return dummy.next

    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next


if __name__ == "__main__":
    node, node.next, node.next.next, node.next.next.next = (
        ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    )

    retVal = Solution().swapPairs(node)
    print("{0} -> {1} -> {2} -> {3}".format(
        retVal.val,
        retVal.next.val,
        retVal.next.next.val,
        retVal.next.next.next.val
    ))
