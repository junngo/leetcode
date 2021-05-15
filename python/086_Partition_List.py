"""
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode(None)
        right_head = ListNode(None)
        left = left_head
        right = right_head

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        right.next = None
        left.next = right_head.next

        return left_head.next


if __name__ == "__main__":
    ln, ln.next, ln.next.next, ln.next.next.next, ln.next.next.next.next, ln.next.next.next.next.next = \
        ListNode(1), ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)

    result = Solution().partition(ln, 3)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(
        result.val,
        result.next.val,
        result.next.next.val,
		result.next.next.next.val,
        result.next.next.next.next.val,
        result.next.next.next.next.next.val))
