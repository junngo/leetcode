# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next


if __name__ == "__main__":
    ln, ln.next, ln.next.next, ln.next.next.next, ln.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    
    ret = Solution().reverseBetween(ln, 2, 4)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(
        ret.val,
        ret.next.val,
		ret.next.next.val,
		ret.next.next.next.val,
        ret.next.next.next.next.val)
    )
