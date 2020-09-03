"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


if __name__ == "__main__":
    ln, ln.next, ln.next.next, ln.next.next.next, ln.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)

    ret = Solution().reverseList(ln)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(
        ret.val,
        ret.next.val,
		ret.next.next.val,
		ret.next.next.next.val,
        ret.next.next.next.next.val)
    )
