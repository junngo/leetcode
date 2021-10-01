# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        idx, node = 0, head
        while node:
            idx += 1
            node = node.next

        if k <= 1 or idx < k:
            return head

        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt

        head.next = self.reverseKGroup(cur, k)

        return node


if __name__ == "__main__":
    head = [1,2,3,4,5]
    head, head.next, head.next.next, head.next.next.next, head.next.next.next.next  = (
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    )
    k = 2
    result = Solution().reverseKGroup(head, k)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(
        result.val,
        result.next.val,
        result.next.next.val,
        result.next.next.next.val,
        result.next.next.next.next.val
    ))
