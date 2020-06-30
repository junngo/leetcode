'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        for idx, val in enumerate(nums):
            if target == val:
                if len(result) == 2:
                    result.pop()

                result.append(idx)

        if len(result) == 1:
            return [result[0], result[0]]

        elif len(result) == 2:
            return result

        else:
            return [-1, -1]


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    ret = Solution().searchRange(nums, target)
    print(ret)
