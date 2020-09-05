"""
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

import heapq
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


if __name__ == "__main__":
    ln1, ln1.next, ln1.next.next = ListNode(1), ListNode(2), ListNode(5)
    ln2, ln2.next, ln2.next.next = ListNode(3), ListNode(6), ListNode(7)
    ln3, ln3.next = ListNode(2), ListNode(6)

    input = [ln1, ln2, ln3]
    ret = Solution().mergeKLists(input)
    print("{0} -> {1} -> {2} -> {3} -> {4} -> {5}".format(
        ret.val,
        ret.next.val,
        ret.next.next.val,
        ret.next.next.next.val,
        ret.next.next.next.next.val,
        ret.next.next.next.next.next.val,
    ))
