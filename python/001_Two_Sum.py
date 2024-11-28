"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target
For example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find_data = target - nums[i]
            idx = i+1

            if find_data in nums[idx:]:
                return [i, nums[idx:].index(find_data)+idx]


if __name__ == '__main__':
	print(Solution().twoSum([2, 7, 11, 15], 9))
