import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)


    def search_bisect(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


if __name__ == "__main__":
    # ex = [-1,0,3,5,9,12]
    ret = Solution().search_bisect([-1, 0, 3, 5, 9, 12, 6], 9)
    print(ret)
