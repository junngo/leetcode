from typing import List

class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     dist = 0
    #     ret_val = {}
    #     nums.sort()

    #     for i_idx, i_val in enumerate(nums):

    #         for j_idx, j_val in enumerate(nums[i_idx+1:]):

    #             if len(nums[i_idx+j_idx+2:]) == 0:
    #                 continue

    #             sum_num = i_val + j_val + nums[i_idx+j_idx+2]
    #             dist = abs(target - sum_num)
    #             ret_val[sum_num] = dist

    #     return min(ret_val, key=ret_val.get)

    def threeSumClosest(self, nums, target):        
        nums.sort()
        result, min_diff = 0, float('inf')

        for index in range(len(nums)-1):
        	left = index + 1
        	right = len(nums) - 1

        	while left < right:
        		currSum = nums[index] + nums[left] + nums[right]
        		diff = abs(target - currSum)

        		if diff == 0:
        			return target
        		if diff < min_diff:
        			min_diff = diff
        			result = currSum

        		if currSum < target:
        			left += 1
        		else:
        			right -= 1

        return result

if __name__ == '__main__':
    result = Solution().threeSumClosest([1,2,4,8,16,32,64,128], 82)
    print(result)
