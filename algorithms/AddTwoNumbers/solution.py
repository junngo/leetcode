'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		retNode = ListNode(0)
		headNode = retNode
		tempVal = 0
		carry = 0

		while(l1 or l2):
			if(l1):
				tempVal += l1.val
				l1 = l1.next

			if(l2):
				tempVal += l2.val
				l2 = l2.next

			carry, tempVal = divmod(tempVal, 10)

			retNode.next = ListNode(tempVal)
			retNode = retNode.next
			tempVal = carry

		if(carry==1):
			retNode.next = ListNode(1)

		return headNode.next

if __name__ =='__main__':
	lN1, lN1.next, lN1.next.next = ListNode(2), ListNode(4), ListNode(3)
	lN2, lN2.next, lN2.next.next = ListNode(5), ListNode(6), ListNode(4)

	resultVar = Solution().addTwoNumbers(lN1, lN2)

	print("{0} -> {1} -> {2}".format(resultVar.val, resultVar.next.val, resultVar.next.next.val))
