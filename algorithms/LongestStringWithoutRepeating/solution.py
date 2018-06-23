'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		tempString = ""
		retStringList = []
		sameFlag = 0

		for i in range(0, len(s)):
			for j in range(0, len(tempString)):
				if(s[i] == tempString[j]):
					retStringList.append(tempString)
					tempString = tempString[j+1:]
					break

			tempString += s[i]

		retStringList.append(tempString)

		return len(max(retStringList, key=len))

if __name__=='__main__':
	lenOfString = Solution().lengthOfLongestSubstring('abcabcbb')
	print(lenOfString)
