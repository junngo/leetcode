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
        idx = 0
        temp_str = ''
        ret_palindorme = []


        for i in s:
            idx += 1
            temp_str = i
            ret_palindorme.append(temp_str)

            for j in s[idx:]:
                temp_str += j

                #  checking palindrome
                if temp_str[:] == temp_str[::-1]:
                    ret_palindorme.append(temp_str)

        return max(ret_palindorme, key=len, default='')

if __name__=='__main__':
	resultStr = Solution().longestPalindrome("a")
	print(resultStr)
