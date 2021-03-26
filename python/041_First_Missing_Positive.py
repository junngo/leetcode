"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = 1

        nums.sort()
        for num in nums:
            if num == result:
                result += 1

        return result


if __name__ == "__main__":
    nums = [1, 2, 0]

    value = Solution().firstMissingPositive(nums)
    print(value)
