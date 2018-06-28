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
        retPalindrome = []

        if len(s) > 1000:
            return

        for i in range(0, len(s)):
            for j in range(i, len(s)+1):
                if (self.palindromeCheckFunc(s[i:j]) == 1) and (s[i:j]):
                    retPalindrome.append(s[i:j])

        return max(retPalindrome, key=len)

    def palindromeCheckFunc(self, str):
        for i in range(0, len(str)/2):
            if str[i] is str[len(str)-1-i]:
                pass
            else:
                return

        return 1

if __name__=='__main__':
	resultStr = Solution().longestPalindrome("cbbd")
	print(resultStr)
