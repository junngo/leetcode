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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp_str, palindorme = "", []

        for idx, ch in enumerate(s):
            temp_str = ch
            palindorme.append(temp_str)

            for j in s[idx+1:]:
                temp_str += j

                #  checking palindrome
                if temp_str[:] == temp_str[::-1]:
                    palindorme.append(temp_str)

        return max(palindorme, key=len, default='')


if __name__=='__main__':
	resultStr = Solution().longestPalindrome("a")
	print(resultStr)
