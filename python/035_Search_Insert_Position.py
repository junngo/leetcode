'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1
'''
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp_idx = 0

        for idx, val in enumerate(nums):
            if target == val:
                return idx
            elif val < target:
                temp_idx = idx+1

        return temp_idx


if __name__ == "__main__":
    li = [1,3,5,6]
    find = 2

    ret = Solution().searchInsert(li, find)
    print(ret)
