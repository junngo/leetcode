'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Notice that the solution set must not contain duplicate quadruplets.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [], target = 0
Output: []
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()

        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left, right = j+1, len(nums)-1

                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if target == temp:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                    elif temp < target:
                        left += 1

                    else:
                        right -= 1

        return result


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    result = Solution().fourSum(nums, 0)
    print(result)
