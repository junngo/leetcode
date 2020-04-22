from typing import List

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     ret_list = []

    #     if len(nums) < 3:
    #         return ret_list

    #     for i_idx, i_val in enumerate(nums):

    #         for j_idx, j_val in enumerate(nums[i_idx+1:]):
    #             find_val = (i_val+j_val) * -1

    #             if find_val in nums[i_idx + j_idx + 1:]:
    #                 temp_list = sorted([i_val, j_val, find_val])
    #                 if temp_list not in ret_list:
    #                     ret_list.append(temp_list)

    #                 break

    #     return ret_list

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_list = []
        ll = len(nums)

        nums.sort()
        
        for i in range(ll - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = ll - 1

            while j < k:
                cur = nums[i] + nums[j] + nums[k]

                if cur == 0:
                    ret_list.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j]==nums[j+1]:
                        j += 1
                    while j < k and nums[k]==nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                
                elif cur < 0:
                    j += 1
                else:
                    k -= 1
        
        return ret_list

if __name__ == '__main__':
    result = Solution().threeSum([1,2,-2,-1])
    print(result)
