'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
'''

from typing import List

class Solution:
    def productExceptSelf_timeout(self, nums: List[int]) -> List[int]:
        temp = list(nums)
        multi = 1
        ret = []

        for idx, val in enumerate(nums):
            temp.pop(idx)
            for i in temp:
                multi = multi * i

            ret.append(multi)
            multi = 1
            temp = list(nums)

        return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out


if __name__ == "__main__":
    value = [1, 2, 3, 4]
    out = Solution().productExceptSelf(value)
    print(out)
