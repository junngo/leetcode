'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):

		toStr = str(x)
		tempList = []
		minusFlag = False

		if toStr[0] is '-':
			minusFlag = True

		for i in toStr:
			tempList.append(i)

		tempList.reverse()
		if minusFlag is True:
			tempList.insert(0, '-')
			tempList.pop()

		retNum = int("".join(tempList))

		if(abs(retNum) > ((1 << 31) - 1)):
			return 0
		else:
			return retNum

if __name__=='__main__':
	retNum = Solution().reverse(-120)
	print(retNum)
