'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
	def lengthOfLongestSubstring(self, s: str) -> int:
		idx_i, idx_j = 0, 0
		long_str = ''
		result = []

		for str_i in s:
			long_str = str_i
			idx_i += 1

			for str_j in s[idx_i:]:
				if s[idx_i+idx_j] in long_str:
					break

				else:
					long_str += str_j
					idx_j += 1

			result.append(long_str)
			idx_j = 0

		return len(max(result, key=len, default=''))

	def lengthOfLongestSubstring_hashtable(self, s: str) -> int:
		used = {}
		max_length = start = 0
		for index, char in enumerate(s):
			if char in used and start <= used[char]:
				start = used[char] + 1
			else:
				max_length = max(max_length, index - start + 1)

			used[char] = index
		
		return max_length


if __name__=='__main__':
	lenOfString = Solution().lengthOfLongestSubstring_hashtable('tmmzuxt')
	print(lenOfString)
