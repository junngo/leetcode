'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	# def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	# 	headNode = ListNode(0)
	# 	headNode.next = head
	# 	node_len = 0

	# 	while(head):
	# 		head = head.next
	# 		node_len += 1

	# 	remove_node_idx = node_len - n
	# 	head = headNode.next

	# 	i = 0
	# 	while(head):
	# 		if i == remove_node_idx-1:
	# 			head.next = head.next.next
	# 		else:
	# 			head = head.next

	# 		i += 1

	# 	return headNode.next

	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		def index(node):
			if not node:
				return 0

			i = index(node.next) + 1

			if i > n:
				node.next.val = node.val

			return i

		index(head)

		return head.next

if __name__ =='__main__':
	lN1, lN1.next, lN1.next.next, lN1.next.next.next, lN1.next.next.next.next = (
		ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5))

	resultVar = Solution().removeNthFromEnd(lN1, 3)

	print("{0} -> {1} -> {2} -> {3}".format(
		resultVar.val,
		resultVar.next.val,
		resultVar.next.next.val,
		resultVar.next.next.next.val)
	)
