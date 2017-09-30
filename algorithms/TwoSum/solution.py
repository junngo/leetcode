"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target
For example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
	def twoSum(self, nums, target):
		for i in range(0, len(nums)-1):
			for j in range(i+1, len(nums)):
				if(nums[i]+ nums[j] == target):
					return [i, j]
		return "no matching num"

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
