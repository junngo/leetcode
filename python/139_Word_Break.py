"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [True]
        for i in range(1, len(s)+1):
            result += any(result[j] and s[j:i] in wordDict for j in range(i)),
            print(result)

        return result[-1]

if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    # s = "leetcode"
    # wordDict = ["leet","code"]
    result = Solution().wordBreak(s, wordDict)
