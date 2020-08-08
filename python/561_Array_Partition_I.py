'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4

Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair = []
        sum = 0
        
        for i in nums:
            pair.append(i)

            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum


if __name__ == "__main__":
    input_val = [1,4,3,2]
    ret = Solution().arrayPairSum(input_val)
    print(ret)
