'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
	def lengthOfLongestSubstring(self, s: str) -> int:
		idx = 0
		loop2_idx = 0
		temp_str = ''
		long_str = []

		for loop_str in s:
			temp_str = loop_str
			idx += 1

			for loop2_str in s[idx:]:
				if s[idx+loop2_idx] in temp_str:
					break
				else:
					temp_str += loop2_str
					loop2_idx += 1

			long_str.append(temp_str)
			loop2_idx = 0

		return len(max(long_str, key=len, default=''))

if __name__=='__main__':
	lenOfString = Solution().lengthOfLongestSubstring('')
	print(lenOfString)
