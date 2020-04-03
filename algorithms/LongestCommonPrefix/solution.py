'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

from typing import List

class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        ret = ''
        find_word = ''
        find_idx = 0
        temp_cnt = 0

        if strs == []:
            return ret

        sort_str = sorted(strs, key=len)
        my_str = sort_str[0]
        sort_str = sort_str[1:]

        for i in my_str:
            find_word += i

            for j in sort_str:
                if find_word == j[:find_idx+1]:
                    temp_cnt += 1

            if temp_cnt == len(sort_str):
                ret = find_word
            if find_idx == 0 and ret =='':
                break

            temp_cnt = 0
            find_idx += 1

        return ret


    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for idx, val in enumerate(shortest):
            for other in strs:
                if other[idx] != val:
                    return shortest[:idx]

        return shortest


if __name__ =='__main__':
    ret = Solution().longestCommonPrefix2(["dog","racecar","car"])
    print(ret)
