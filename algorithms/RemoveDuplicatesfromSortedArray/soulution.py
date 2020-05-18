'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = []

        for i_idx, i_val in enumerate(nums):
            if i_val not in nums[i_idx+1:]:
                ret.append(i_val)

        nums[:] = ret
        return len(nums)

if __name__ == "__main__":
    ret = Solution().removeDuplicates([1, 1, 2])
    print(ret)
