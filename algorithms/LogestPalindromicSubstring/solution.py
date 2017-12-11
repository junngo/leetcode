'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
	'''
		tempStr		   = ""
		palindromeStr  = []
		palindromeFlag = 0
		curPosition    = 0

		for i in range(0, len(s)):
			tempStr += s[i]
			
			for j in range(0, len(tempStr)/2):
				if tempStr[j] == tempStr[len(tempStr)-1-j]:
					palindromeFlag = 1
					curPosition    = j
				else:
					palindromeFlag = 0

			if(palindromeFlag == 1):
				palindromeStr.append(tempStr[:len(tempStr)])
				palindromeFlag = 0
				tempStr = tempStr[len(tempStr)-1]

		return max(palindromeStr)
	'''

if __name__=='__main__':
	resultStr = Solution().longestPalindrome('cbbd')
	print(resultStr)
