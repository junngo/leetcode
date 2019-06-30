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


	def twoSum2(self, nums, target):
		j = 0

		for i in nums:
			find_data = target - i
			j += 1
			temp_nums = nums[j:]

			if find_data in temp_nums:
				return [j-1, temp_nums.index(find_data)+j]


if __name__ == '__main__':
	#print(Solution().twoSum([2, 7, 11, 15], 9))
	print(Solution().twoSum2([2, 7, 11, 15], 9))
