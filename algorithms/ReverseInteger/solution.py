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
class Solution:
	def reverse(self, x: int) -> int:
		minus_flag = False
		pos_limit = 0x7fffffff
		neg_limit =-0x80000000

		if x < 0:
			x *= -1
			minus_flag = True

		num = int(str(x)[::-1])

		if minus_flag:
			num *= -1
			if (num & neg_limit) == neg_limit:
				return num

		else:
			if (num & pos_limit) == num:
				return num

		return 0

if __name__=='__main__':
	retNum = Solution().reverse(-123)
	print(retNum)
